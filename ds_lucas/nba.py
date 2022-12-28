from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import teams
from nba_api.stats.static import players


# Challenge: find Curry id
from nba_api.stats.static import players
# get_players returns a list of dictionaries, each representing a player.
nba_players = players.get_players()
# print('Number of players fetched: {}'.format(len(nba_players)))
nba_players[:5]
nba_players_active = [player for player in nba_players if player.get("is_active") == True]
curry_info = [i for i in nba_players_active if i.get("full_name") == "Stephen Curry"]
curry_id = curry_info[0].get("id")
# print(curry_id)
# print(type(curry_id))


# Curry career data
career = playercareerstats.PlayerCareerStats(player_id=curry_id)
df_raw = career.get_data_frames()[0]
print(df_raw.columns)
df_clean = df_raw[['SEASON_ID', 'PLAYER_AGE', 'GP', 'GS', 'MIN', 'FGM', 'FGA', 'FG3M', 'FG3A',
                   'FTM', 'FTA', 'OREB', 'DREB', 'AST', 'STL',
                   'BLK', 'TOV', 'PTS']]



print(df_clean.head())