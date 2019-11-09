import os
import codecs
import time
import urllib
from urllib.request import build_opener, HTTPCookieProcessor
from urllib.parse import urlencode
import http
from http.cookiejar import CookieJar
import json
from util.squid_api import NintendoNetAPI
from util.make_dataset import MakeDataset

                     
if __name__ == '__main__':
    print('Please ensure the cookie works.')
    
    # [CAUTION] iksm_session will be expired in two or three days.
    cookie = 'iksm_session=4be8c9847a72aa56147342d996e61705f90677f0'
    
    # [CAUTION] Do not include a trailing slash.
    url_personal_data = 'https://app.splatoon2.nintendo.net/api/results'
    
    # Get Battle data from nintendo net 
    nintendo_net_api = NintendoNetAPI(cookie, url_personal_data)
    nintendo_net_api.save_battle_data()
    
    print(f'{nintendo_net_api.updated_file_count} files are loaded.')
    
    # Gathering battle data
    make_dataset = MakeDataset()
    make_dataset.gather_battle_data();
    
    print('save to csv file.')
    
    
    