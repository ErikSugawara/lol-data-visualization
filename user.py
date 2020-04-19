from riotwatcher import LolWatcher, ApiError
import pandas as pd
import numpy as np

class User:

    def __init__(self, region, name, watcher):
        self.region = region
        self.name = name
        self.watcher = watcher
        self.user_info = self.watcher.summoner.by_name(self.region, self.name)
        self.match_information()

    def kda(self):
        '''
        Returns Dataframe of KDA in participant matche
        '''
        # List of participants name/info
        summoners_name = []
        participants = []

        # Getting names of participants
        for row in self.match_detail['participantIdentities']:
            names_row = {}
            names_row['Name'] = row['player']['summonerName']
            summoners_name.append(names_row)
        name = [x['Name'] for x in summoners_name]

        # Getting KDA
        for row in self.match_detail['participants']:
            participants_row = {}
            participants_row['kills'] = row['stats']['kills']
            participants_row['deaths'] = row['stats']['deaths']
            participants_row['assists'] = row['stats']['assists']
            participants.append(participants_row)

        df = pd.DataFrame(participants, index=name)
        print(df)

        return df

    def match_information(self):
        # Getting information about match
        self.matches = self.watcher.match.matchlist_by_account(self.region,
                                                               self.user_info['accountId'])
        last_match = self.matches['matches'][0]
        self.match_detail = self.watcher.match.by_id(self.region,
                                                     last_match['gameId'])

