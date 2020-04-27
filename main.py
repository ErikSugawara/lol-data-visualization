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
        # Information about user and match
        user = User('br1', 'hdef', self.watcher)
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

        try:
            user.current_match_information()
        except ApiError:
            print("The user is not current in a match.")
        plt.show()


def main():
    api_key = 'RGAPI-a0d8b830-5989-464b-a27c-0e7faf16e310'
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

