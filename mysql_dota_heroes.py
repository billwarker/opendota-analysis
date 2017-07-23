import requests
from bs4 import BeautifulSoup
import json
import pymysql

print('Starting...')

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='Greengiant90',
						db='mysql', charset='utf8')
cur = conn.cursor()
cur.execute('USE dota_stats')

# API Query for Heroes
sess = requests.Session()
html = r"https://api.opendota.com/api/heroes"
response = sess.get(html)

content = response.content.decode("utf-8")
heroes = json.loads(content)

for hero in heroes:
	position = {'Carry': 0,
				'Jungler': 0,
			 	'Pusher': 0,
			 	'Nuker': 0,
			 	'Disabler': 0,
			 	'Initiator': 0,
			 	'Escape': 0,
			 	'Durable': 0,
			 	'Support': 0}

	for role in hero['roles']:
		position[role] += 1

	query = """INSERT INTO dota_heroes (id, name, localized_name,
										primary_attr, attack_type, 
										carry, jungler, pusher, nuker,
										disabler, initiator, durable,
										support, legs) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
	cur.execute(query, (hero['id'], hero['name'], hero['localized_name'], hero['primary_attr'],
						hero['attack_type'], position['Carry'], position['Jungler'], position['Pusher'],
						position['Nuker'], position['Disabler'], position['Initiator'], position['Durable'], position['Support'], hero['legs']))
	conn.commit()
	print('Added {}.'.format(hero['localized_name']))

# Close MySQL Database
cur.close()
conn.close()
print('Done.')