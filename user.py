import pandas as pd
import datetime as dt

class User:

    def __init__(self, region, name, watcher):
        self.region = region
        self.name = name
        self.watcher = watcher
        self.user_info = self.watcher.summoner.by_name(self.region, self.name)
        self.accountId = self.user_info['accountId']
        self.summonerId = self.user_info['id']
        self.matches = self.watcher.match.matchlist_by_account(self.region,
                                                               self.accountId
                                                               )['matches']
    def games_played_in_lane(self):
        '''
        Include ARAM Games as None
        Bottom = ADC/Support
        '''
        top = 0
        jungle = 0
        mid = 0
        bottom = 0
        none = 0
        lanes = ['Top', 'Jungle', 'Mid', 'Bottom', 'None']
        for match in self.matches:
            if match['lane'] == 'TOP':
                top += 1
            if match['lane'] == 'JUNGLE':
                jungle += 1
            if match['lane'] == 'MID':
                mid += 1
            if match['lane'] == 'BOTTOM':
                bottom += 1
            if match['lane'] == 'NONE':
                none += 1

        df = pd.DataFrame([top, jungle, mid, bottom, none], index=lanes)
        return df


    def kda_matches_classic(self):
        '''Returns a dataframe of user kda on ten last games in classic mode'''
        kda_detail = []
        # matches_date = []
        for match in self.matches[:10]:
            match_id = match['gameId']
            match_info = self.watcher.match.by_id(self.region, match_id)
            if self.is_valid_match(match_info) is True:
                kda_detail.append(self.kda(match_info))
                # matches_date.append(dt.datetime.fromtimestamp(match_info['gameCreation']).isoformat())
        df = pd.concat(kda_detail)
        print(df)
        return df

    def kda(self, match_detail):
        user_kda = []
        user_id = self.user_id_match(match_detail)
        for row in match_detail['participants']:
            if row['participantId'] == user_id:
                kda_row = {}
                kda_row['kills'] = row['stats']['kills']
                kda_row['deaths'] = row['stats']['deaths']
                kda_row['assists'] = row['stats']['assists']
                user_kda.append(kda_row)
        df = pd.DataFrame(user_kda)
        # Death column without zero, because of division by zero when death = 0
        deaths_no_zero = [1 if x == 0 else x for x in df['deaths']]
        kda_values = (df['kills'] + df['assists'])/deaths_no_zero
        df['KDA'] = pd.DataFrame(kda_values, index=df.index)
        print(df)
        return df

    def user_id_match(self, match_detail):
        # Getting user id in a match
        for row in match_detail['participantIdentities']:
            if row['player']['summonerName'] == self.name:
                return row['participantId']

    def is_valid_match(self, match):
        if (match['gameMode'] == 'CLASSIC' and
            match['gameType'] == 'MATCHED_GAME' and
            match['gameDuration'] >= 900):
            return True
        return False

