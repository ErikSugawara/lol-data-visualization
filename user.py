import pandas as pd

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
        # Getting KDA
        participants = []
        for row in self.match_detail['participants']:
            participants_row = {}
            participants_row['kills'] = row['stats']['kills']
            participants_row['deaths'] = row['stats']['deaths']
            participants_row['assists'] = row['stats']['assists']
            participants.append(participants_row)
        df = pd.DataFrame(participants, index=self.name)
        # Death column without zero, because of division by zero when death = 0
        deaths_no_zero = [1 if x == 0 else x for x in df['deaths']]
        kda_values = (df['kills'] + df['assists'])/deaths_no_zero
        df['KDA'] = pd.DataFrame(kda_values, index=df.index)
        print(df)
        return df

    def damage_dealt_mitigated(self):
        # Getting KDA
        participants = []
        for row in self.match_detail['participants']:
            participants_row = {}
            participants_row['Total DMG Champions'] = row['stats']['totalDamageDealtToChampions']
            participants_row['Damage mitigated'] = row['stats']['damageSelfMitigated']
            participants.append(participants_row)
        df = pd.DataFrame(participants, index=self.name)
        print(df)
        return df

    def ward_score(self):
        participants = []
        for row in self.match_detail['participants']:
            participants_row = {}
            participants_row['Placed'] = row['stats']['wardsPlaced']
            participants_row['Removed'] = row['stats']['wardsKilled']
            participants_row['Vision Score'] = row['stats']['visionScore']
            participants.append(participants_row)
        df = pd.DataFrame(participants, index=self.name)
        print(df)
        return df

    def match_information(self):
        # Getting information about match
        self.matches = self.watcher.match.matchlist_by_account(self.region,
                                                               self.user_info['accountId'])
        last_match = self.matches['matches'][1]
        self.match_detail = self.watcher.match.by_id(self.region,
                                                     last_match['gameId'])
        print(self.match_detail['gameMode'])
        # List of participants name/info
        summoners_name = []
        # Getting names of participants
        for row in self.match_detail['participantIdentities']:
            names_row = {}
            names_row['Name'] = row['player']['summonerName']
            summoners_name.append(names_row)
        self.name = [x['Name'] for x in summoners_name]


