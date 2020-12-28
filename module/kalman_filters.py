import numpy as np
from numpy import sqrt, trace, zeros, identity
from numpy.linalg import inv

# ============================
# Linear Kalman Filter
# ============================
"""
TODO: 説明
状態空間モデル
x[t] = Mx[t-1] + Gu[t]
y[t] = Hx[t-1] + w[t]
"""       
class LinearKalmanFilter:
    def __init__(self, M, H, G, Q, R, y, x_0, P_0, dt=0.05, delta=1e-3, alpha=1):
        self.M = M
        self.G = G
        self.H = H
        self.Q = Q
        self.R = R
        self.y = y
        self.dt = dt
        self.dim_x = x_0.shape[0]
        self.P = P_0
        self.trP = []
        self.x_a = x_0
        self.x = []
        self.delta = delta
        self.alpha = alpha # 1以上
        
  # 逐次推定を行う
    def forward_estimation(self):
        for y_obs in self.y:
            self._forecast()
            self._update(y_obs)

    # 更新/解析
    def _update(self, y_obs):
        self.P = self.alpha*self.P # 乗法的
        P = self.P; H = self.H
                
        # Kalman gain
        K = P@H.T@inv(H@P@H.T + self.R)
        
        # 誤差共分散更新
        self.P -= K@H@P

        # x 更新
        self.x_a = self.x_f + K@(y_obs - H@self.x_f)

        # 更新した値を保存
        self.x.append(self.x_a)
        self.trP.append(sqrt(trace(self.P)/self.dim_x)) # traceを正規化して保存

    # 予報/時間発展
    def _forecast(self, log=False):
        x_a = self.x_a; M = self.M; N = self.dim_x
        
        # 予報
        self.x_f = self.M@x_a
        
        # self.P = M@self.P@M.T + self.G@self.Q@(self.G.T)
        self.P = M@self.P@M.T + self.Q[0]*self.G@(self.G.T)

        if log:
            self.x.append(self.x_f)
    
    # 追加の推定(観測値なし)
    def additional_forecast(self, step):
        for _ in range(step):
            self._forecast(log=True)

# ============================
# Extended Kalman Filter
# ============================
"""
TODO: 説明
非線形のモデルに拡張したKalman Filter
状態空間モデル
x[t] = M(x[t-1]) + G(u[t])
y[t] = Hx[t-1] + w[t]
"""    
class ExtendedKalmanFilter:
    def __init__(self, M, H, G, Q, R, y, x_0, P_0, dt=0.05, delta=1e-3, alpha=1):
        self.M = M
        self.G = G
        self.H = H
        self.Q = Q
        self.R = R
        self.y = y
        self.dt = dt
        self.dim_x = x_0.shape[0]
        self.P = P_0
        self.trP = []
        self.x_a = x_0
        self.x = []
        self.delta = delta
        self.alpha = alpha # 1以上
        
  # 逐次推定を行う
    def forward_estimation(self):
        for y_obs in self.y:
            self._forecast()
            self._update(y_obs)

    # 更新/解析
    def _update(self, y_obs):
        self.P = self.alpha*self.P # 乗法的
        P = self.P

        H = self.H
                
        # Kalman gain
        K = P@H.T@inv(H@P@H.T + self.R)
        
        # 誤差共分散更新
        self.P -= K@H@P

        # x 更新
        self.x_a = self.x_f + K@(y_obs - H@self.x_f)

        # 更新した値を保存
        self.x.append(self.x_a)
        self.trP.append(sqrt(trace(self.P)/self.dim_x)) # traceを正規化して保存

    # 予報/時間発展
    def _forecast(self, log=False):
        x_a = self.x_a; dt = self.dt; M = self.M; N = self.dim_x
        
        # 予報
        self.x_f = self.M(x_a, dt)
        
        # 線形化， dtを大きくするとうまくいかなくなる
        JM = zeros((N, N))
        for j in range(N):
            dx = self.delta*identity(N)[:, j]
            JM[:, j] = (M(x_a + dx, dt) - self.x_f)/self.delta # ここでJM[:, j] = (M(x_a + dx, dt) - self.M(x_a, dt))/self.deltaとするとすごく遅くなる

        # self.P = JM@self.P@JM.T + self.G@self.Q@(self.G.T)
        self.P = JM@self.P@JM.T + self.Q[0]*self.G@(self.G.T)

        if log:
            self.x.append(self.x_f)
    
    # 追加の推定(観測値なし)
    def additional_forecast(self, step):
        for _ in range(step):
            self._forecast(log=True)