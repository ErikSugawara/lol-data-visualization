from riotwatcher import LolWatcher, ApiError
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from user import User
from match import Match
from current_match import CurrentMatch

class LolDataVisualization:

    def __init__(self, api_key):
        self.watcher = LolWatcher(api_key)

    def plot_chart(self):
        # Information about user and match
        user = User('br1', 'Magafo', self.watcher)
        match_info = user.matches[0]
        match_id = match_info['gameId']
        match_detail = self.watcher.match.by_id(user.region, match_id)
        match = Match(match_detail)
        # KDA
        kda_df = match.kda()
        kda_df.plot(kind='barh')
        # Damage dealt/mitigated
        dmg_df = match.damage_dealt_mitigated()
        dmg_df.plot(kind='barh')
        # Total Farm
        farm_df = match.total_farm()
        farm_df.plot(kind='barh')
        # ARAM Games does not have wards
        if match.match_detail['gameMode'] == 'CLASSIC':
            ward_df = match.ward_score()
            ward_df.plot(kind='barh')

        plt.show()

    def plot_kda_user_matches(self):
        user = User('br1', 'hdef', self.watcher)
        user.games_played_in_lane().plot(kind='bar')
        user.kda_classic_matches().plot(kind='bar')
        user.dmg_classic_matches().plot(kind='bar')
        plt.show()

def main():
    api_key = 'RGAPI-2008d312-2c94-4b83-bedb-b6b99c8e4d63'
    lol = LolDataVisualization(api_key)
    # lol.plot_chart()
    lol.plot_kda_user_matches()


if __name__ == "__main__":
    main()
