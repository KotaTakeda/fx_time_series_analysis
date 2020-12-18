"""
解析に使う関数をまとめる．

以下で読み込む
import sys
sys.path.append('./module')
from utils import *
"""

import numpy as np
import pandas as pd

# logの差分を取る関数とその逆関数
def log_diff(arr):
    return np.array([np.log(arr[0]), *np.diff(np.log(arr))])

def log_diff_inv(log_diff_arr):
    return np.exp(np.cumsum(log_diff_arr), dtype=float)

def load_fx_data(instrument_list, data_kind='train'):
    df_dict = {}
    for instrument in instrument_list:
        df = pd.read_csv(f'data/fx_data_{instrument}_{data_kind}', index_col=0, header=0)
        df.index = pd.to_datetime(df.index)
        df_dict[instrument] = df
    return df_dict