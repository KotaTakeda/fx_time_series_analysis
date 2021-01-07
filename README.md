# fxデータの時系列解析
開発中です．

# コード
## `data_analysis.ipynb`
fxデータから何らかの特性を見出すために様々な解析を行っています．

## `time_series_model.ipynb`
基本的な時系列モデルである自己回帰(AR)モデル，移動平均(MA)モデルを使って時系列データの生成をしています．

## `state_system.ipynb`
`time_series_model.ipynb`で扱っていたモデルを状態空間モデルの言葉で書き直し，同様にデータを生成しています．

## `kalman_filter.ipynb`
`state_system.ipynb`で作ったモデルとデータを使ってKalman Filterによる双子実験行っています．


# 参考
- [Kalman Filter](https://github.com/KotaTakeda/rccs_online_school)
