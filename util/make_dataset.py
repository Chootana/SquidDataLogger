#%%
import os
import json
import csv
from datetime import datetime


class MakeDataset:
    
    def __init__(self):
        self.output_dir_path = './data/dataset'
        self.battle_dir_path = './data/results'
        self.time_stamp = datetime.now().strftime('%Y%m%d%H')
        self.output_file_path = self.output_dir_path + '/' + self.time_stamp + '-all.csv'    
        
        if not os.path.isdir(self.output_dir_path):
            os.makedirs(self.output_dir_path)
        
    def data_formatting(self, input_file):
        
        data = json.load(input_file)
        data_list = [
            # summary data
            data['battle_number'],
            data['game_mode']['name'],
            data['rule']['name'],
            data['stage']['name'],
            #data['estimate_x_power'],
            data['my_team_result']['name'],
            data['my_team_count'],
                
            # my result
            data['player_result']['player']['nickname'],
            data['player_result']['player']['weapon']['name'],
            data['player_result']['player']['weapon']['special']['name'],
            data['player_result']['player']['weapon']['sub']['name'],
            data['player_result']['kill_count'],
            data['player_result']['assist_count'],
            data['player_result']['death_count'],
            data['player_result']['special_count'],
            data['player_result']['game_paint_point']
                ]
            
            # my members' results without my result
        for player in data['my_team_members']:
            data_list.append(player['player']['nickname'])
            data_list.append(player['player']['weapon']['name'])
            data_list.append(player['player']['weapon']['special']['name'])
            data_list.append(player['player']['weapon']['sub']['name'])
            data_list.append(player['kill_count'])
            data_list.append(player['assist_count'])
            data_list.append(player['death_count'])
            data_list.append(player['special_count'])
            data_list.append(player['game_paint_point'])
            
        for player in data['other_team_members']:
            data_list.append(player['player']['nickname'])
            data_list.append(player['player']['weapon']['name'])
            data_list.append(player['player']['weapon']['special']['name'])
            data_list.append(player['player']['weapon']['sub']['name'])
            data_list.append(player['kill_count'])
            data_list.append(player['assist_count'])
            data_list.append(player['death_count'])
            data_list.append(player['special_count'])
            data_list.append(player['game_paint_point'])
            
        return data_list
    
    def gather_battle_data(self):
    
        with open(self.output_file_path, 'w', encoding='utf_8_sig') as output_file:
            writer = csv.writer(output_file, lineterminator='\n')
        
            files = os.listdir(self.battle_dir_path)
            hidden_file = '.DS_Store'
            if hidden_file in files:
                files.remove(hidden_file)

            for file in files:
                self.input_file_path = self.battle_dir_path + '/' + file
                with open(self.input_file_path, 'r') as input_file:
                    data_list = self.data_formatting(input_file) 
                    writer.writerow(data_list)
