import pandas as pd

class User:

    def __init__(self, region, name, watcher):
        self.region = region
        self.name = name
        self.watcher = watcher
        self.user_info = self.watcher.summoner.by_name(self.region, self.name)
        self.accountId = self.user_info['accountId']
        self.summonerId = self.user_info['id']

