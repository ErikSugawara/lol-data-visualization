from riotwatcher import LolWatcher, ApiError
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from user import User

class LolDataVisualization:

    def __init__(self):
        api_key = 'RGAPI-60e701e2-2b18-4559-a056-233247c37852'
        self.watcher = LolWatcher(api_key)

    def plot_chart(self):
        user = User('br1', 'Jukes', self.watcher)
        kda_df = user.kda()
        kda_df.plot(kind='barh')
        dmg_df = user.damage_dealt_mitigated()
        dmg_df.plot(kind='barh')
        farm_df = user.total_farm()
        farm_df.plot(kind='barh')
        # ARAM Games does not have wards
        if user.match_detail['gameMode'] == 'CLASSIC':
            ward_df = user.ward_score()
            ward_df.plot(kind='barh')

        user.current_match_information()
        plt.show()


def main():
    lol = LolDataVisualization()
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

