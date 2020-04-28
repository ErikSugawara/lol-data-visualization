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
                                                               self.accountId)['matches']

    def current_match_information(self):
        self.current_match = self.watcher.spectator.by_summoner(self.region,
                                                                self.summonerId)
        self.participants_information()

    def win_match_probability(self):
        # Parameters: (KDA, Vision Score, Farm, Dmg Dealt/Mitigate)
        # of 5 last game of each participant.
        pass

    # TODO: Get data from last five games, using current role and game mode classic.
    # TODO: Function to get average of each paramenter in a match
    def win_lane_probability(self):
        pass

    def participants_information(self):
        self.current_participants = []
        self.current_participants_info = []
        self.matches_participants = []
        for row in self.current_match['participants']:
            self.current_participants.append(row['summonerName'])

        for participant_name in self.current_participants:
            participant_info = self.watcher.summoner.by_name(self.region, participant_name)
            self.current_participants_info.append(participant_info)

        for participant_id in self.current_participants_info:
            matches = self.watcher.match.matchlist_by_account(self.region, participant_id['accountId'])['matches']
            self.matches_participants.append(matches)
        print(self.current_participants_info)

