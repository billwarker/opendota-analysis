--- Export to CSV file ---

SELECT result, radiant_win, duration, start_time, game_mode,
		localized_name, kills, deaths, assists, primary_attr,
		attack_type, carry, jungler, pusher, nuker, disabler,
		initiator, durable, support, legs

FROM dota_matches JOIN dota_heroes ON (hero_id=id)

INTO OUTFILE "C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/dota_stats.csv"
FIELDS TERMINATED BY ','
TERMINATED BY ','
LINES TERMINATED BY '\n';