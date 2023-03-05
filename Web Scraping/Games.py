import requests
import pandas as pd
import numpy as np
import datetime

k = 28
game_list = []

# While loop that goes through and scrapes each game's final score for the month of February
while k > 0:
    
    # Sets k as a string to use in the url variable
    s = str(k)
    
    # Since the date for single digits dates is 0# this if loop sends s to the correct url
    if k > 9:
        url = "https://www.cbssports.com/college-basketball/scoreboard/FBS/202302" + s + "/"
    else:
        url = "https://www.cbssports.com/college-basketball/scoreboard/FBS/2023020" + s + "/"
    games = pd.DataFrame()

    html = requests.get(url).content
    ppg2022_list = pd.read_html(html)
    games1 = pd.DataFrame()

    for instance in ppg2022_list:
        games1 = games1.append(instance, ignore_index=True)
    games = pd.concat([games, games1])
    
    # Cleans the data through dropping columns and Nan values
    games = games.drop([0, '1', '2', 'OT', 'Unnamed: 1'], axis=1, errors='ignore')
    games = games.dropna(subset=['Unnamed: 0', "T"])
    games = games.dropna()
    
    # Since the data separates the game scores, this is where the rows are combined
    data = games.to_numpy().reshape(-1, 2)
    new_data = []
    for i in range(0,len(data),2):
        new_data.append(list(data[i]) + list(data[i+1]))
    
    # Create a new DataFrame with four columns
    games = pd.DataFrame(new_data, columns=['Visitor', 'Vscore', 'Home', 'Hscore'])

    # If games are cancelled the order of the columns are mixed up, these next lines solve that issue
    if games['Home'].dtype == float:
        # Reorders the columns
        games[['Visitor', 'Vscore', 'Home', 'Hscore']] = games[['Vscore', 'Visitor', 'Hscore', 'Home']].values
    
    # The original values had the teams record in them, so these lines clean out any number, then remove the 
    # dash that remains as the last character on each team name
    games['Visitor'] = games['Visitor'].str.replace('\d+', '', regex=True)
    games['Home'] = games['Home'].str.replace('\d+', '', regex=True)
    games['Visitor'] = games['Visitor'].str.slice(stop=-1)
    games['Home'] = games['Home'].str.slice(stop=-1)
    
    # Stores the games from the specific date to a list that allows each day to be concatenated into one data frame
    game_list.append(games)
    k = k - 1

# Here is where the dataframe is concatenated
FebGames = pd.concat(game_list, ignore_index=True)

k = 31
game_list = []

# While loop that goes through and scrapes each game's final score for the month of January
while k > 0:
    
    # Sets k as a string to use in the url variable
    s = str(k)
    
    # Since the date for single digits dates is 0# this if loop sends s to the correct url
    if k > 9:
        url = "https://www.cbssports.com/college-basketball/scoreboard/FBS/202301" + s + "/"
    else:
        url = "https://www.cbssports.com/college-basketball/scoreboard/FBS/2023010" + s + "/"
    games = pd.DataFrame()

    html = requests.get(url).content
    ppg2022_list = pd.read_html(html)
    games1 = pd.DataFrame()

    for instance in ppg2022_list:
        games1 = games1.append(instance, ignore_index=True)
    games = pd.concat([games, games1])
 
    # Cleans the data through dropping columns and Nan values
    games = games.drop([0, '1', '2', 'OT', 'Unnamed: 1'], axis=1, errors='ignore')
    games = games.dropna(subset=['Unnamed: 0', "T"])
    games = games.dropna()
    
    # Since the data separates the game scores, this is where the rows are combined   
    data = games.to_numpy().reshape(-1, 2)
    new_data = []
    for i in range(0,len(data),2):
        new_data.append(list(data[i]) + list(data[i+1]))
        
    # Create a new DataFrame with four columns
    games = pd.DataFrame(new_data, columns=['Visitor', 'Vscore', 'Home', 'Hscore'])
 
    # If games are cancelled the order of the columns are mixed up, these next lines solve that issue
    if games['Home'].dtype == float:
        # Reorders the columns
        games[['Visitor', 'Vscore', 'Home', 'Hscore']] = games[['Vscore', 'Visitor', 'Hscore', 'Home']].values
    
    # The original values had the teams record in them, so these lines clean out any number, then remove the 
    # dash that remains as the last character on each team name
    games['Visitor'] = games['Visitor'].str.replace('\d+', '', regex=True)
    games['Home'] = games['Home'].str.replace('\d+', '', regex=True)
    games['Visitor'] = games['Visitor'].str.slice(stop=-1)
    games['Home'] = games['Home'].str.slice(stop=-1)
    
    # Stores the games from the specific date to a list that allows each day to be concatenated into one data frame
    game_list.append(games)
    k = k - 1

# Here is where the dataframe is concatenated
JanGames = pd.concat(game_list, ignore_index=True)

k = 31
game_list = []

# While loop that goes through and scrapes each game's final score for the month of December
while k > 0:
    
    # Sets k as a string to use in the url variable
    s = str(k)
    
    # Since the date for single digits dates is 0# this if loop sends s to the correct url
    if k > 9:
        url = "https://www.cbssports.com/college-basketball/scoreboard/FBS/202212" + s + "/"
    else:
        url = "https://www.cbssports.com/college-basketball/scoreboard/FBS/2022120" + s + "/"
    games = pd.DataFrame()

    html = requests.get(url).content
    ppg2022_list = pd.read_html(html)
    games1 = pd.DataFrame()

    for instance in ppg2022_list:
        games1 = games1.append(instance, ignore_index=True)
    games = pd.concat([games, games1])
    
    # Cleans the data through dropping columns and Nan values
    games = games.drop([0, '1', '2', 'OT', 'Unnamed: 1'], axis=1, errors='ignore')
    games = games.dropna(subset=['Unnamed: 0', "T"])
    games = games.dropna()

    # Since the data separates the game scores, this is where the rows are combined
    data = games.to_numpy().reshape(-1, 2)
    new_data = []
    for i in range(0,len(data),2):
        new_data.append(list(data[i]) + list(data[i+1]))

    # Create a new DataFrame with four columns
    games = pd.DataFrame(new_data, columns=['Visitor', 'Vscore', 'Home', 'Hscore'])
    
    # If games are cancelled the order of the columns are mixed up, these next lines solve that issue
    if games['Home'].dtype == float:
        # Reorders the columns
        games[['Visitor', 'Vscore', 'Home', 'Hscore']] = games[['Vscore', 'Visitor', 'Hscore', 'Home']].values
    
    # The original values had the teams record in them, so these lines clean out any number, then remove the 
    # dash that remains as the last character on each team name
    games['Visitor'] = games['Visitor'].str.replace('\d+', '', regex=True)
    games['Home'] = games['Home'].str.replace('\d+', '', regex=True)
    games['Visitor'] = games['Visitor'].str.slice(stop=-1)
    games['Home'] = games['Home'].str.slice(stop=-1)
    
    # Stores the games from the specific date to a list that allows each day to be concatenated into one data frame
    game_list.append(games)
    k = k - 1
    # December 26th had no games played, the next two lines allows the code to skip that day
    if k == 26:
        k = k - 1

# Here is where the dataframe is concatenated
DecGames = pd.concat(game_list, ignore_index=True)

k = 30
game_list = []

# While loop that goes through and scrapes each game's final score for the month of November
while k > 6:
    
    # Sets k as a string to use in the url variable
    s = str(k)
    
    # Since the date for single digits dates is 0# this if loop sends s to the correct url
    if k > 9:
        url = "https://www.cbssports.com/college-basketball/scoreboard/FBS/202211" + s + "/"
    else:
        url = "https://www.cbssports.com/college-basketball/scoreboard/FBS/2022110" + s + "/"
    games = pd.DataFrame()

    html = requests.get(url).content
    ppg2022_list = pd.read_html(html)
    games1 = pd.DataFrame()

    for instance in ppg2022_list:
        games1 = games1.append(instance, ignore_index=True)
    games = pd.concat([games, games1])
    
    # Cleans the data through dropping columns and Nan values
    games = games.drop([0, '1', '2', 'OT', 'Unnamed: 1'], axis=1, errors='ignore')
    games = games.dropna(subset=['Unnamed: 0', "T"])
    games = games.dropna()
    
    # Since the data separates the game scores, this is where the rows are combined
    data = games.to_numpy().reshape(-1, 2)
    new_data = []
    for i in range(0,len(data),2):
        new_data.append(list(data[i]) + list(data[i+1]))

    # Create a new DataFrame with four columns
    games = pd.DataFrame(new_data, columns=['Visitor', 'Vscore', 'Home', 'Hscore'])
    
    # If games are cancelled the order of the columns are mixed up, these next lines solve that issue
    if games['Home'].dtype == float:
        # Reorders the columns 
        games[['Visitor', 'Vscore', 'Home', 'Hscore']] = games[['Vscore', 'Visitor', 'Hscore', 'Home']].values
    
    # The original values had the teams record in them, so these lines clean out any number, then remove the 
    # dash that remains as the last character on each team name
    games['Visitor'] = games['Visitor'].str.replace('\d+', '', regex=True)
    games['Home'] = games['Home'].str.replace('\d+', '', regex=True)
    games['Visitor'] = games['Visitor'].str.slice(stop=-1)
    games['Home'] = games['Home'].str.slice(stop=-1)
    
    # Stores the games from the specific date to a list that allows each day to be concatenated into one data frame
    game_list.append(games)
    k = k - 1
    if k == 26:
        k = k - 1

# Here is where the dataframe is concatenated
NovGames = pd.concat(game_list, ignore_index=True)

# Concatenates all months of games
GameScores = pd.concat([NovGames, DecGames, JanGames, FebGames], ignore_index=True)
GameScores