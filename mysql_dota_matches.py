import requests
from bs4 import BeautifulSoup
import json
import pymysql

print('Starting...')

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='Greengiant90',
						db='mysql', charset='utf8')
cur = conn.cursor()
cur.execute('USE dota_stats')

# API Query for Wins
account_id = 94818894
games_won = {"win": 1} # Games I won

sess = requests.Session()
html = r"https://api.opendota.com/api/players/{}/matches".format(account_id)
response = sess.get(html, params=games_won)

content = response.content.decode("utf-8")
wins = json.loads(content)

# API Query for Losses
games_lost = {"win": 0} # Games I lost
response = sess.get(html, params=games_lost)

content = response.content.decode("utf-8")
losses = json.loads(content)

# Write Wins into MySQL
total_matches = len(wins) + len(losses)
count = 1
for match in wins:

	query = """INSERT INTO dota_matches (match_id, player_slot,
										 radiant_win, duration,
										 game_mode, lobby_type,
										 hero_id, start_time,	#13
										 version, kills,
										 deaths, assists, skill, result) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,1)""" # 1 = Win
	cur.execute(query, (match['match_id'], match['player_slot'],
						match['radiant_win'], match['duration'],
						match['game_mode'], match['lobby_type'],
						match['hero_id'], match['start_time'],
						match['version'], match['kills'],
						match['deaths'], match['assists'], match['skill']))
	conn.commit()
	print('Match {} of {} added.'.format(count, total_matches))
	count += 1

# Write Losses into MySQL
for match in losses:

	query = """INSERT INTO dota_matches (match_id, player_slot,
										 radiant_win, duration,
										 game_mode, lobby_type,
										 hero_id, start_time,	#13
										 version, kills,
										 deaths, assists, skill, result) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,0)""" # 0 = Loss
	cur.execute(query, (match['match_id'], match['player_slot'],
						match['radiant_win'], match['duration'],
						match['game_mode'], match['lobby_type'],
						match['hero_id'], match['start_time'],
						match['version'], match['kills'],
						match['deaths'], match['assists'], match['skill']))	
	conn.commit() #13
	print('Match {} of {} added.'.format(count, total_matches))
	count += 1

# Close MySQL Database
cur.close()
conn.close()
print('Done.')