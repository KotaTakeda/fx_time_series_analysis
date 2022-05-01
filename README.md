# fxデータの時系列解析
作成者：竹田航太

fx時系列データに対していくつかの手法を使って予測を試みた記録です．
あまり複雑なモデル使用せずfxデータの特徴を理解することを目的としています．

# データ
|見出し|説明|
|---|---|
|通貨ペア| USDJPY, GBRJPY, EURJPY|
|開始| 2014/01/01|
|終了| 2019/12/31|
|間隔 | 1日|
|内容|買値(ask)と売値(bid)それぞれで始値，終値，高値，安値,出来高を取得|

## `data/`
oanda APIを使って取得したfxデータが保存されています．
### `img/`
データ解析や予測結果のpngデータが入っています．

# コード
## `data_analysis/`
### `data_analysis.ipynb`
fxデータから何らかの特性を見出すために様々な解析を行っています．

### `component_decomposition.ipynb`
KFで成分分解モデルにより解析を試みています．

## `model_tutorials/`
### `time_series_model.ipynb`
基本的な時系列モデルである自己回帰(AR)モデル，移動平均(MA)モデルを使って時系列データの生成をしています．

### `state_system.ipynb`
`time_series_model.ipynb`で扱っていたモデルを状態空間モデルの言葉で書き直し，同様にデータを生成しています．

### `kalman_filter.ipynb`
`state_system.ipynb`で作ったモデルとデータを使ってKalman Filterによる双子実験行っています．

## `forecast/`
### `arma_to_fx.ipynb`
ARMAモデルを使ってfxデータの状態推定，フィッティングを行います．

### `rnn_to_fx.ipynb`
RNNを使ってfxデータにフィッティング，予測を行います．

# LICENCE
[LICENCE](https://github.com/KotaTakeda/fx_time_series_analysis/blob/main/LICENCE)

# 参考
- [Kalman Filter](https://github.com/KotaTakeda/rccs_online_school)
