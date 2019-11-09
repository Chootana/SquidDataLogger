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
    def __init__(self, cookie, url_personal_data):
        self.cookie = cookie
        self.url = url_personal_data
        self.url_battle_data_array = []
        self.updated_file_count = 0
        
        self.json_personal_data = self.get_json_data(url_personal_data);
        self.set_battle_numbers()
        
    def save_battle_data(self):
        output_dir_path = './data/results'
        for result in self.json_personal_data['results']:
            battle_number_str = result['battle_number']
            url_battle_data = self.url + '/' + battle_number_str
            output_file_path = output_dir_path + '/result-battle-' + battle_number_str + '.json'
            if not os.path.exists(output_file_path):
                print(f'new: {url_battle_data}')
                self.json_battle_data = self.get_json_data(url_battle_data)
                self.save_json_data(self.json_battle_data, output_dir_path, output_file_path)
                
                # To get all results takes about 4min (50results * 5s)
                time.sleep(1)
    
    def get_json_data(self, url):
        opener = build_opener(HTTPCookieProcessor(CookieJar()))
        opener.addheaders.append(('Cookie', self.cookie))
        response = opener.open(url)
        return json.load(response)
    
    def set_battle_numbers(self):
        for result in self.json_personal_data['results']:
            battle_number_str = result['battle_number']
            url_battle_data = self.url + '/' + battle_number_str
            self.url_battle_data_array.append(url_battle_data)
        
    def save_json_data(self, data, output_dir_path, output_file_path):
        if not os.path.isdir(output_dir_path):
                os.makedirs(output_dir_path)
                
        if not(os.path.exists(output_file_path)):
                self.updated_file_count += 1
                outputFile = codecs.open(output_file_path, 'w', encoding='utf-8')
                json.dump(data, outputFile, ensure_ascii=False, indent=4, sort_keys=True)
                outputFile.close()
            
                     
if __name__ == '__main__':
    print('Please ensure the cookie works.')
    
    # [CAUTION] iksm_session will be expired in two or three days.
    cookie = 'iksm_session=4be8c9847a72aa56147342d996e61705f90677f0'
    
    # [CAUTION] Do not include a trailing slash.
    url_personal_data = 'https://app.splatoon2.nintendo.net/api/results'
    
    nintendo_net_api = NintendoNetAPI(cookie, url_personal_data)
    nintendo_net_api.save_battle_data()
    
    print(f'{nintendo_net_api.updated_file_count} files are loaded.')
    
    
    
    