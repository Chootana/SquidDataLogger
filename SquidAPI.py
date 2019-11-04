import urllib
from urllib.request import build_opener, HTTPCookieProcessor
from urllib.parse import urlencode
import http
from http.cookiejar import CookieJar
import json
import os
import codecs
import time


class NintendoNetAPI():
    def __init__(self, cookie, url_summary_data):

        self.cookie = cookie
        self.url = url_summary_data
        self.url_battle_data_array = []
        self.json_personal_data = self.get_json_data(url_summary_data);
        
        self.set_battle_numbers()
        
        # [TODO] get_json_data -> self.json_data
        # [CAUTION] to investigate how many times we can access each url
    
    def get_json_data(self, url):
        opener = build_opener(HTTPCookieProcessor(CookieJar()))
        opener.addheaders.append(("Cookie", cookie))
        response = opener.open(url)
        return json.load(response)
    
    def set_battle_numbers(self):
        for result in self.json_personal_data["results"]:
            battle_number_str = result['battle_number']
            url_battle_data = self.url + '/' + battle_number_str
            self.url_battle_data_array.append(url_battle_data)
        
                
    def save_json_data(self, data, output_dir_path, output_file_path):
        if not os.path.isdir(output_dir_path):
                os.makedirs(output_dir_path)
                
        if not(os.path.exists(output_file_path)):
                outputFile = codecs.open(output_file_path, "w", encoding="utf-8")
                json.dump(data, outputFile, ensure_ascii=False, indent=4, sort_keys=True)
                outputFile.close()
                
        # [TODO]
        # adding counting function which says how many files are made. If there is no updating, it returns asserted comments like "no results are updated" or "Something wrong... Isiksm_sessionexpired?".

    def save_all_data(self):
        # old version
        output_dir_path = "./data/all"
        output_file_path = output_dir_path + "/all.json"
        self.save_json_data(self.json_data, output_dir_path, output_file_path)
        
    def save_battle_data(self):
        output_dir_path = "./data/personal_results"
        for result in self.json_data["results"]:
            output_file_path = output_dir_path + "/result-personal-" + result["battle_number"] + ".json"
            self.save_json_data(result, output_dir_path, output_file_path)
            
    def save_detailed_battle_data(self):
        output_dir_path = "./data/results"
        for url in self.url_battle_data_array:
            print("update: " + url)
            self.json_battle_data = self.get_json_data(url)
            output_file_path = output_dir_path + "/result-battle-" + self.json_battle_data["battle_number"] + ".json"
            self.save_json_data(self.json_battle_data, output_dir_path, output_file_path)
            
            # To prevent frequent access to api (Roughly 1sec?)
            time.sleep(1)
            
            
    
        
        
    
    
if __name__ == '__main__':
    # [CAUTION] iksm_session will be expired in two or three days.
    cookie = "iksm_session=e58e25d155891b4255f49b37e771c614038ae24d"
    
    # [CAUTION] Do not include a trailing slash.
    url_summary_data = "https://app.splatoon2.nintendo.net/api/results"
    
    # [TODO] to get battle_number and get detailed battle data.
    nintendo_net_api = NintendoNetAPI(cookie, url_summary_data)
    nintendo_net_api.save_detailed_battle_data()
    # nintendo_net_api.get_json_data()
    # nintendo_net_api.save_battle_data()
    # nintendo_net_api.save_all_data()
    
    