## データの差し込みタイプで簡単にペラのHTMLを生成する

- _incフォルダの中身（差し込むデータをつくる）
- test_.py（差し込むデータをつくる）
- template.txt（差し込まれるデータ、読み込むデータ用のテンプレートをつくる）



## pipからjinja2パッケージをインストール

すでにインストールしている場合は不要

pip3 install jinja2


## pythonプログラムを実行

python3 test_.py


## 参考にしたページ

https://karupoimou.hatenablog.com/entry/2019/05/20/112231


## pythonプログラムを実行して output-2.txt にファイル出力

print(str(html))

python3 test_.py > output-2.txt


## 環境

- パソコン: X230（Lenovo ThinkPad）
- OS: Linux Mint 20.3（Xfce）
- Python 3.8.10

