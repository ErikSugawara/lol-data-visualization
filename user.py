import pandas as pd
import datetime as dt
from match import Match

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
        None = ARAM and events which doesn't have a lane.
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

    # TODO: Add game duration parameter.
    def kda_classic_matches(self):
        '''Returns a dataframe of the user kda on his ten latest games in classic mode'''
        kda_detail = []
        for match in self.matches[:10]:
            match_id = match['gameId']
            match_detail = self.watcher.match.by_id(self.region, match_id)
            if self.is_valid_match(match_detail) is True:
                match = Match(match_detail)
                user_kda = match.kda().loc[self.name, ['assists', 'deaths', 'kills', 'KDA']]
                # TODO: Verify proper way to do this.
                kda_detail.append(pd.DataFrame(user_kda).T.reset_index())
        df = pd.concat(kda_detail)
        return df

    def dmg_classic_matches(self):
        dmg_detail = []
        for match in self.matches[:10]:
            match_id = match['gameId']
            match_detail = self.watcher.match.by_id(self.region, match_id)
            if self.is_valid_match(match_detail) is True:
                match = Match(match_detail)
                user_dmg = match.damage_dealt_mitigated().loc[self.name, ['Total DMG Champions',
                                                                          'Damage mitigated']]
                # TODO: Verify proper way to do this.
                dmg_detail.append(pd.DataFrame(user_dmg).T.reset_index())
        df = pd.concat(dmg_detail)
        return df

    def is_valid_match(self, match):
        if (match['gameMode'] == 'CLASSIC' and
            match['gameType'] == 'MATCHED_GAME' and
            match['gameDuration'] >= 900):
            return True
        return False

