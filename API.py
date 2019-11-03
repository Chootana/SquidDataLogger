import urllib
from urllib.request import build_opener, HTTPCookieProcessor
from urllib.parse import urlencode
import http
from http.cookiejar import CookieJar
import json
import os
import codecs

# 引数のURL(Splatoon API)にアクセス、レスポンスのJSONデータをreturn
def getJson(url): # UrlにアクセスしJsonを取得
    cookie = "iksm_session=3f5e5e5a01280ddc032db39a652c342bd3137238"
    opener = build_opener(HTTPCookieProcessor(CookieJar()))
    opener.addheaders.append(("Cookie", cookie))
    res = opener.open(url)
    return json.load(res)


    
# 引数のJSONデータ(戦績データを期待)を戦績ごとにファイルに保存
def saveButtleResults(jsonData):
    for result in jsonData["results"]:
        
        # 戦績保存用ディレクトリの作成
        outputDirectoryPath = "./results"
        if not os.path.isdir(outputDirectoryPath):
            os.makedirs(outputDirectoryPath)
        # この戦績に対応するファイル名とパスを組み立てる
        #soutputFilePath = "./results/result-buttle-" + result["battle_number"] + ".json"
        outputFilePath = "./result" + result["battle_number"] + ".json"
        # この戦績ファイルが既に存在するか確認、なかったら作成・書き込み
        if not(os.path.exists(outputFilePath)) :
            outputFile = codecs.open(outputFilePath, "w", encoding="utf-8")
            json.dump(result, outputFile, ensure_ascii=False, indent=4, sort_keys=True)
            outputFile.close()

saveButtleResults(getJson("https://app.splatoon2.nintendo.net/api/records"))