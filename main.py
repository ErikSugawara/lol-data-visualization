from riotwatcher import LolWatcher, ApiError
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from user import User
from match import Match

class LolDataVisualization:

    def __init__(self, api_key):
        self.watcher = LolWatcher(api_key)

    def plot_chart(self):
        user = User('br1', 'hdef', self.watcher)
        match = Match(user, self.watcher)
        kda_df = match.kda()
        kda_df.plot(kind='barh')
        dmg_df = match.damage_dealt_mitigated()
        dmg_df.plot(kind='barh')
        farm_df = match.total_farm()
        farm_df.plot(kind='barh')
        # ARAM Games does not have wards
        if match.match_detail['gameMode'] == 'CLASSIC':
            ward_df = match.ward_score()
            ward_df.plot(kind='barh')

        try:
            match.current_match_information()
        except ApiError:
            print("The user is not current in a match.")
        plt.show()


def main():
    api_key = 'RGAPI-30a7b792-5295-4af5-a135-43c2e12e8158'
    lol = LolDataVisualization(api_key)
    lol.plot_chart()


if __name__ == "__main__":
    main()

    '''
    (MID_LANE, SOLO):MIDDLE
    (TOP_LANE, SOLO):TOP
    (JUNGLE, NONE):JUNGLE
    (BOT_LANE, DUO_CARRY):BOTTOM
    (BOT_LANE, DUO_SUPPORT):UTILITY
    '''

    # latest = watcher.data_dragon.versions_for_region(my_region)['n']['champion']
    # static_champ_list = watcher.data_dragon.champions(latest, False, 'en_US')

    # champ_dict = {}
    # for key in static_champ_list['data']:
    #   row = static_champ_list['data'][key]
    #   champ_dict[row['key']] = row['id']

    # for row in participants:
    #   print(str(row['champion']) + ' ' + champ_dict[str(row['champion'])])
    #  row['championName'] = champ_dict[str(row['champion'])]

