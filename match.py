import pandas as pd

class Match:

    def __init__(self, user, watcher):
        self.user = user
        self.wtr = watcher
        self.match_information()

    def kda(self):
        '''
        Returns Dataframe of KDA in participant match
        '''
        # Getting KDA
        participants = []
        for row in self.match_detail['participants']:
            participants_row = {}
            participants_row['kills'] = row['stats']['kills']
            participants_row['deaths'] = row['stats']['deaths']
            participants_row['assists'] = row['stats']['assists']
            participants.append(participants_row)
        df = pd.DataFrame(participants, index=self.participants_name)
        # Death column without zero, because of division by zero when death = 0
        deaths_no_zero = [1 if x == 0 else x for x in df['deaths']]
        kda_values = (df['kills'] + df['assists'])/deaths_no_zero
        df['KDA'] = pd.DataFrame(kda_values, index=df.index)
        print(df)
        return df

    def damage_dealt_mitigated(self):
        participants = []
        for row in self.match_detail['participants']:
            participants_row = {}
            damage_dealt = row['stats']['totalDamageDealtToChampions']
            damage_mitigated = row['stats']['damageSelfMitigated']
            participants_row['Total DMG Champions'] = damage_dealt
            participants_row['Damage mitigated'] = damage_mitigated
            participants.append(participants_row)
        df = pd.DataFrame(participants, index=self.participants_name)
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
        df = pd.DataFrame(participants, index=self.participants_name)
        print(df)
        return df

    def total_farm(self):
        participants = []
        for row in self.match_detail['participants']:
            participants_row = {}
            participants_row['Farm'] = row['stats']['totalMinionsKilled']
            participants.append(participants_row)
        df = pd.DataFrame(participants, index=self.participants_name)
        print(df)
        return df

    def current_match_information(self):
        self.current_match = self.wtr.spectator.by_summoner(self.user.region,
                                                            self.user.summonerId)
        print(self.current_match)

    def win_match_probability(self):
        # Parameters: (KDA, Vision Score, Farm, Dmg Dealt/Mitigate) of 5 last games

    def match_information(self):
        # Getting information about match
        self.matches = self.wtr.match.matchlist_by_account(self.user.region,
                                                           self.user.accountId)
        last_match = self.matches['matches'][0]
        self.match_detail = self.wtr.match.by_id(self.user.region,
                                                 last_match['gameId'])
        print(self.match_detail)
        # List of participants name/info
        summoners_name = []
        # Getting names of participants
        for row in self.match_detail['participantIdentities']:
            names_row = {}
            names_row['Name'] = row['player']['summonerName']
            summoners_name.append(names_row)
        self.participants_name = [x['Name'] for x in summoners_name]


