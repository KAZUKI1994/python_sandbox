# coding: utf-8
import json

# set json file exported from trello at current directory
f = open('file.json', 'r')
data = json.load(f)

# 
# getting members
# 
members = {}
for member in data['members']:
	member_id = member['id']
	member_name = member['fullName']
	members.update({member_id: member_name})

#
# getting lists
#
lists = {}
for list in data['lists']:
	list_id = list['id']
	list_name = list['name']
	lists.update({list_id: list_name})

#
#  getting cards
#  
counter = 1
print "項番, ステータス, カード名, 説明, 担当者, 更新日時"
for card in data['cards']:
	closed = card['closed']
	if (closed == True):
		updated_date = card['dateLastActivity']
		desc = card['desc']
		card_id = card['id']
		title = card['name']
		asigned_member_ids = card['idMembers']
		list_id = card['idList']

		# asigned_member_name
		if len(asigned_member_ids) > 0:
			asigned_member_id = asigned_member_ids[0]
			asigned_member_name = members[asigned_member_id]
		else:
			asigned_member_name = ""

		# list_name
		list_name = lists[list_id]

		print str(counter) + ", " + list_name + ", " + title + ", " + desc + ", " + asigned_member_name + ", " + updated_date
		counter = counter + 1
