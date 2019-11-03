import urllib
from urllib.request import build_opener, HTTPCookieProcessor
from urllib.parse import urlencode
import http
from http.cookiejar import CookieJar
import json
import os
import codecs

class NintendoNetAPI():
    def __init__(self, cookie, url):
        self.cookie = cookie
        self.url = url
    
    def get_json_data(self):
        opener = build_opener(HTTPCookieProcessor(CookieJar()))
        opener.addheaders.append(("Cookie", cookie))
        res = opener.open(url)
        from IPython import embed; embed(); exit()
        self.json_data = json.load(res)
    
    def save_json_data(self, data, output_dir_path, output_file_path):
        if not os.path.isdir(output_dir_path):
                os.makedirs(output_dir_path)
                
        if not(os.path.exists(output_file_path)):
                outputFile = codecs.open(output_file_path, "w", encoding="utf-8")
                json.dump(data, outputFile, ensure_ascii=False, indent=4, sort_keys=True)
                outputFile.close()

    def save_all_data(self):
        output_dir_path = "all"
        output_file_path = output_dir_path + "/all.json"
        self.save_json_data(self.json_data, output_dir_path, output_file_path)
        
    def save_battle_data(self):
        output_dir_path = "./results"
        from IPython import embed; embed(); exit()
        for result in self.json_data["results"]:
            output_file_path = output_dir_path + "/result-battle-" + result["battle_number"] + ".json"
            self.save_json_data(result, output_dir_path, output_file_path)
            
    
        
        
    
    
if __name__ == '__main__':
    cookie = "iksm_session=3195c9548b278b3ca0c6b3a17c5d556d682b3a81"
    url = "https://app.splatoon2.nintendo.net/api/data/results/"
    
    nintendo_net_api = NintendoNetAPI(cookie, url)
    nintendo_net_api.get_json_data()
    nintendo_net_api.save_battle_data()
    nintendo_net_api.save_all_data()
    
    