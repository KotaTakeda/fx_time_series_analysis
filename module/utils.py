"""
解析に使う関数をまとめる．

以下で読み込む
import sys
sys.path.append('./module')
from utils import *
"""

import numpy as np
import pandas as pd

def log_diff(arr):
    """
    対数値の差分をとる．
    args: 
        - arr: 配列
    return:
        - arrの初項の対数値とarrの対数差分
    """
    return np.array([np.log(arr[0]), *np.diff(np.log(arr))])

def log_diff_inv(log_diff_arr):
    """
    log_difの逆関数になっている．
    args: 
        - log_diff_arr: 配列, log_difで作った配列や対数差分をの空間で推定した配列
    """
    return np.exp(np.cumsum(log_diff_arr), dtype=float)

def load_fx_data(instrument_list, data_kind='train', path_to_data='..'):
    """
    fxデータをローカルから読み込み．
    args:
        - instrument_list: 文字配列, 為替ペア名の配列('USD_JPY', 'GBP_JPY', 'EUR_JPY')
        - data_kind: 読み込みたいデータの種類．('train', 'test')
    return:
        df_fict: dict, 為替ペア名をkeyとしたfxデータの辞書
    """
    df_dict = {}
    for instrument in instrument_list:
        df = pd.read_csv(f'{path_to_data}/data/fx_data_{instrument}_{data_kind}', index_col=0, header=0)
        df.index = pd.to_datetime(df.index)
        df_dict[instrument] = df
    return df_dict

def cum_std(series):
    """
    累積標準偏差
    args:
        - series: np.ndarray (N,), 時系列データ
    return:
        cum_std: np.ndaray (N,), 時系列データの累積標準偏差
    """
    cum_std = [np.std(series[:n]) for n in range(series.shape[0])]
    return np.array(cum_std)

def nrmse(true, esti, nomalize_const=1.):
    """
    正規化RMSE
    args:
        - true: np.ndarray (N,)
        - esti: np.ndarray (N,)
        - nomalize_std: float > 0, 正規定数
    return:
        nrmse: float
    """
    true = true.reshape(-1,); esti = esti.reshape(-1,)
    return np.linalg.norm(true-esti, ord=2)/np.sqrt(len(true))/nomalize_const