SELECT localized_name, primary_attr, attack_type, carry,
		jungler, pusher, nuker, disabler, initiator,
		durable, support, legs

FROM dota_heroes

INTO OUTFILE "C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/dota_hero_stats.csv"
FIELDS TERMINATED BY ','
TERMINATED BY ','
LINES TERMINATED BY '\n';