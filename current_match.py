from riotwatcher import ApiError
class CurrentMatch:

    def __init__(self, region, summonerId, watcher):
        self.region = region
        self.summonerId = summonerId
        self.watcher = watcher
        self.current_match_information()

    def current_match_information(self):
        try:
            self.current_match = self.watcher.spectator.by_summoner(self.region,
                                                                    self.summonerId)
            self.participants_information()
        except ApiError:
            print("User is not current in a match")

    def participants_information(self):
        self.name_participants = []
        for row in self.current_match['participants']:
            self.name_participants.append(row['summonerName'])

        print(self.current_match)

