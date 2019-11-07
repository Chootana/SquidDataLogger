import json
import csv
import os

output_dir_path = './data/data_list'
output_file_path = output_dir_path + "/data_list.txt"

if not os.path.isdir(output_dir_path):
    os.makedirs(output_dir_path)
    
with open(output_file_path, 'w') as output_file:
    
    input_file_path = "./data/results/result-battle-8812.json"
    with open(input_file_path, 'r') as input_file:
        data = json.load(input_file)
        
        data_list = [
        data['battle_number'],
        data['game_mode']['name'],
        data['rule']['name'],
        data['stage']['name'],
        data['estimate_x_power'],
        data['my_team_result']['name'],
        data['my_team_count'],
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
        
        # my members' results, not including my result
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

    writer = csv.writer(output_file, lineterminator='\n')
    writer.writerow(data_list)
