import requests
import pandas as pd
import numpy as np
import datetime

url = "https://www.cbssports.com/college-basketball/scoreboard/all/20230215/"

html = requests.get(url).content
ppg2022_list = pd.read_html(html)
print(ppg2022_list[0]['Unnamed: 0'])

# = pd.DataFrame (ppg2022_list, columns = ['product_name', "1", "2", "T"])
games = pd.DataFrame()

for instance in ppg2022_list:
    games = games.append(instance, ignore_index=True)
    
games.drop([108,109],inplace=True)
   
url = "https://www.cbssports.com/college-basketball/scoreboard/all/20230214/"

html = requests.get(url).content
ppg2022_list = pd.read_html(html)
games1 = pd.DataFrame()

for instance in ppg2022_list:
    games1 = games1.append(instance, ignore_index=True)
    

games = pd.concat([games, games1])
games = games.drop(['1', '2', 'OT'], axis=1)

print(games)