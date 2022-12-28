import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Module name: nba-api
from nba_api.stats.endpoints import playercareerstats
# from nba_api.stats.static import teams
from nba_api.stats.static import players


def get_player_info(full_name: str = "Stephen Curry") -> pd.DataFrame:

    nba_players = players.get_players()
    nba_players_active = [
        player for player in nba_players if player.get("is_active") == True]
    curry_info = [i for i in nba_players_active if i.get(
        "full_name") == full_name]
    curry_id = curry_info[0].get("id")
    career = playercareerstats.PlayerCareerStats(player_id=curry_id)
    df_raw = career.get_data_frames()[0]
    df_clean = df_raw[['SEASON_ID', 'PLAYER_AGE', 'GP', 'GS', 'MIN', 'FGM', 'FGA', 'FG3M', 'FG3A',
                       'FTM', 'FTA', 'OREB', 'DREB', 'AST', 'STL',
                       'BLK', 'TOV', 'PTS']]

    return df_clean


if __name__ == "__main__":
    df = get_player_info()
    print(df.head())
