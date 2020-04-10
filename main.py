from riotwatcher import LolWatcher, ApiError
import pandas as pd
import numpy as np

api_key = 'RGAPI-de02c895-ee45-4fcc-a267-390c4987fcc5'
watcher = LolWatcher(api_key)
my_region = 'br1'

me = watcher.summoner.by_name(my_region, 'Magafo')
print(me)

my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])
print(my_ranked_stats)

my_matches = watcher.match.matchlist_by_account(my_region, me['accountId'])
# print(my_matches)

last_match = my_matches['matches'][0]
print(last_match)

match_detail = watcher.match.by_id(my_region, last_match['gameId'])

participants = []

for row in match_detail['participants']:
    participants_row = {}
    participants_row['champion'] = row['championId']
    participants_row['spell1'] = row['spell1Id']
    participants_row['spell2'] = row['spell2Id']
    participants_row['win'] = row['stats']['win']
    participants_row['kills'] = row['stats']['kills']
    participants_row['deaths'] = row['stats']['deaths']
    participants_row['assists'] = row['stats']['assists']
    participants_row['totalDamageDealt'] = row['stats']['totalDamageDealt']
    participants_row['goldEarned'] = row['stats']['goldEarned']
    participants_row['champLevel'] = row['stats']['champLevel']
    participants_row['totalMinionsKilled'] = row['stats']['totalMinionsKilled']
    participants_row['item0'] = row['stats']['item0']
    participants_row['item1'] = row['stats']['item1']
    participants.append(participants_row)

df = pd.DataFrame(participants)
print(df)

latest = watcher.data_dragon.versions_for_region(my_region)['n']['champion']
static_champ_list = watcher.data_dragon.champions(latest, False, 'en_US')

champ_dict = {}

for key in static_champ_list['data']:
    row = static_champ_list['data'][key]
    champ_dict[row['key']] = row['id']

for row in participants:
    print(str(row['champion']) + ' ' + champ_dict[str(row['champion'])])
    row['championName'] = champ_dict[str(row['champion'])]

df = pd.DataFrame(participants)
print(df)
