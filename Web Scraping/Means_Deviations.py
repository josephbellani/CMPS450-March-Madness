import pandas as pd
import numpy as np

GameScores = pd.read_csv("GameScores.csv")

unique_teams = GameScores['Home'].unique()

def team_games(team, df):
    # Filter the dataframe for the team's home games
    home_games = df[df['Home'] == team].reset_index(drop=True)
    
    # Filter the dataframe for the team's away games
    away_games = df[df['Visitor'] == team].reset_index(drop=True)
    
    # Create an empty dataframe with enough columns for all the games
    num_games = len(home_games)+ len(away_games)
    game_df = pd.DataFrame(columns=[team])
    
    # Fill in the home games
    i = 0
    for _, row in home_games.iterrows():
        game_df.loc[i] = row['Hscore']
        i += 1
        
    # Fill in the away games
    for _, row in away_games.iterrows():
        game_df.loc[i] = row['Vscore']
        i += 1

    return game_df.T

PointsFor = pd.DataFrame()

# Loop through each team and append their game scores to the Games dataframe
for team in unique_teams:
    team_games_df = team_games(team, GameScores)
    PointsFor = pd.concat([PointsFor, team_games_df], axis=0)

row_means = PointsFor.mean(axis=1, skipna=True)
row_stds = PointsFor.std(axis=1, skipna=True)

# Add the row means and standard deviations as new columns
PointsFor['Points For'] = row_means
PointsFor['Standard Deviation'] = row_stds

PointsFor = PointsFor.sort_index()

def team_games_against(team, df):
    # Filter the dataframe for the team's home games
    home_games = df[df['Home'] == team].reset_index(drop=True)
    
    # Filter the dataframe for the team's away games
    away_games = df[df['Visitor'] == team].reset_index(drop=True)
    
    # Create an empty dataframe with enough columns for all the games
    num_games = len(home_games)+ len(away_games)
    game_df = pd.DataFrame(columns=[team])
    
    # Fill in the home games
    i = 0
    for _, row in home_games.iterrows():
        game_df.loc[i] = row['Vscore']
        
        i += 1
        
    # Fill in the away games
    for _, row in away_games.iterrows():
        game_df.loc[i] = row['Hscore']
        i += 1

    return game_df.T
PointsAgainst = pd.DataFrame()

# Loop through each team and append their game scores to the Games dataframe
for team in unique_teams:
    team_games_df = team_games_against(team, GameScores)
    PointsAgainst = pd.concat([PointsAgainst, team_games_df], axis=0)

row_means = PointsAgainst.mean(axis=1, skipna=True)

# Add the row means and standard deviations as new columns
PointsAgainst['Points Against'] = row_means

PointsAgainst = PointsAgainst.sort_index()

AllStats = pd.concat([PointsFor[['Points For', 'Standard Deviation']], PointsAgainst['Points Against']], axis=1)
AllStats