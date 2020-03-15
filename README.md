# SquidDataLogger
# Overview
+ イカリング2アプリで使用している戦績取得APIをアプリ外から叩き，個人使用目的で戦績を保存する
+ 味方・敵を含めた戦績を定期的にJSON形式で取得し，自分のプレイを見直す
+ 過去データから将来の勝率を推定する
# Requirement
+ python 3.6.3
+ mitmproxy 4.0.4
+ Nintendo Switch Online/イカリング２

# iOSの設定
1. プロキシサーバーにするマシンと同じネットワークに接続
2. ネットワーク設定の一番下にHTTPプロキシを手動に変更
    1. サーバ: プロキシサーバにするマシンのIPアドレス
    2. ポート: 8080など
    3. 認証: オフ

# Tips
+ wifi，プロキシの設定をしたが，iOSでNintendo Switch Onlineが開けない時

+ mitmproxyからiksm_sessionをコピーする方法
```python
export.clip curl @focus
```