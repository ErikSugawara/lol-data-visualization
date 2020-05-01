import pandas as pd

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
        top = 0
        jungle = 0
        mid = 0
        bottom = 0
        none = 0

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

        return [top, jungle, mid, bottom, none]


    def kda_all_matches(self):
        matches_detail = []
        print(self.matches)
        for match in self.matches[:1]:
            match_id = match['gameId']
            detail = self.watcher.match.by_id(self.region, match_id)
            matches_detail.append(detail)
            print(detail)

    def is_valid_match(self, match):
        if (match['gameMode'] == 'CLASSIC' and
            match['gameType'] == 'MATCHED_GAME' and
            match['gameDuration'] >= 900):
            return True
        return False

