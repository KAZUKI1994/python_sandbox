#! /usr/bin/env python
# coding: utf-8

import sys
import json
import csv


#
# Load Json File from ComandLine argument
#
with open(sys.argv[1], 'r') as f:
	data = json.load(f, strict=False)

# 
# Set members Dictionary
# 
members = {}
for member in data['members']:
	member_id = member['id']
	member_name = member['fullName']
	members.update({member_id: member_name})

#
# Set lists Dictionary
#
lists = {}
for list in data['lists']:
	list_id = list['id']
	list_name = list['name']
	lists.update({list_id: list_name})

#
#  Get cards value
#
tickets = []
for card in data['cards']:
	closed = card['closed']
	if (closed == False):
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

		tickets.append([list_name, title, desc, asigned_member_name, updated_date])


#
# Write CSV
#
with open('trello_cards.csv', 'w', newline='') as csvFile:
	csvwriter = csv.writer(csvFile, delimiter=',',quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
	csvwriter.writerow(['リスト名', 'カード名', '説明', '担当者', '更新日時'])
	for ticket in tickets:
		csvwriter.writerow(ticket)