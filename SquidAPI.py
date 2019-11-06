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
        self.updated_file_count = 0
        
        self.json_summary_data = self.get_json_data(url_summary_data);
        self.set_battle_numbers()
        
        # [TODO] get_json_data -> self.json_data
        # [CAUTION] to investigate how many times we can access each url
    
    def get_json_data(self, url):
        opener = build_opener(HTTPCookieProcessor(CookieJar()))
        opener.addheaders.append(("Cookie", self.cookie))
        response = opener.open(url)
        return json.load(response)
    
    def set_battle_numbers(self):
        for result in self.json_summary_data["results"]:
            battle_number_str = result['battle_number']
            url_battle_data = self.url + '/' + battle_number_str
            self.url_battle_data_array.append(url_battle_data)
        
    def save_json_data(self, data, output_dir_path, output_file_path):
        if not os.path.isdir(output_dir_path):
                os.makedirs(output_dir_path)
                
        if not(os.path.exists(output_file_path)):
                self.updated_file_count += 1
                outputFile = codecs.open(output_file_path, "w", encoding="utf-8")
                json.dump(data, outputFile, ensure_ascii=False, indent=4, sort_keys=True)
                outputFile.close()

    def save_all_data(self):
        output_dir_path = "./data/all"
        output_file_path = output_dir_path + "/result-summary.json"
        self.save_json_data(self.json_summary_data, output_dir_path, output_file_path)
        
    def save_battle_data(self):
        output_dir_path = "./data/personal_results"
        for result in self.json_data["results"]:
            output_file_path = output_dir_path + "/result-personal-" + result["battle_number"] + ".json"
            self.save_json_data(result, output_dir_path, output_file_path)
            
    def save_detailed_battle_data(self):
        output_dir_path = "./data/results"
        for url in self.url_battle_data_array:
            print("new: " + url)
            self.json_battle_data = self.get_json_data(url)
            output_file_path = output_dir_path + "/result-battle-" + self.json_battle_data["battle_number"] + ".json"
            self.save_json_data(self.json_battle_data, output_dir_path, output_file_path)
            
            # To prevent frequent access to api (Roughly 1sec?)
            time.sleep(1)
            
            
if __name__ == '__main__':
    print("Please ensure the cookie works.")
    # [CAUTION] iksm_session will be expired in two or three days.
    cookie = "iksm_session=2b6ecfcc86f8b624ff4b464daa569cb673756d0b"
    
    # [CAUTION] Do not include a trailing slash.
    url_summary_data = "https://app.splatoon2.nintendo.net/api/results"
    
    nintendo_net_api = NintendoNetAPI(cookie, url_summary_data)
    nintendo_net_api.save_detailed_battle_data()
    
    print(f"{nintendo_net_api.updated_file_count} files are loaded.")
    
    