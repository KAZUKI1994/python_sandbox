# coding: utf-8
import json

f = open('kanri_enoteca_tickets.json', 'r')
data = json.load(f)
counter = 1
print "項番, ボード名, カード名, 説明, 担当者, 実装状況"

tasks = [[]]

for i in data['actions']:
	# get value from json
	board_name = i['data']['board']['name']
	if 'card' in i['data']:
		card_id = i['data']['card']['id']
		card_name = i['data']['card']['name']
	else:
		card_id = ""
		card_name = ""

	if 'card' in i['data']:
			if 'desc' in i['data']['card']:
				description = i['data']['card']['desc']
			else:
				description = ""
	else:
		description = ""

	if 'list' in i['data']:
		status = i['data']['list']['name']
	elif 'listAfter' in i['data']:
		status = i['data']['listAfter']['name']
	else:
		status = ""

	if 'memberCreator' in i:
		asignnee = i['memberCreator']['fullName']
	else:
		asignnee = ""

	if 'type' in i:
		type = i['type']
	exists = 0
	for s in tasks:
		if(card_id in s):
			exists = 1
	if exists == 0:
		task = [str(counter), card_id, type, board_name, card_name, description, status]
		tasks.append(task)
		print str(counter) + ", " +board_name + ", " + card_name + "," + description + "," + asignnee + "," + status
		counter = counter + 1
