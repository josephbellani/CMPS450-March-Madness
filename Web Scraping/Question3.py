import requests  
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

url = "https://www.teamrankings.com/ncaa-basketball/stat/points-per-game?date=2022-04-05"

html = requests.get(url).content
ppg2022_list = pd.read_html(html)
ppg2022 = ppg2022_list[0]

url = "https://www.teamrankings.com/ncaa-basketball/stat/opponent-points-per-game?date=2022-04-05"

html = requests.get(url).content
oppPpg2022_list = pd.read_html(html)
oppPpg2022 = oppPpg2022_list[0]
oppPpg2022 = oppPpg2022.drop(oppPpg2022.columns[[0,3,4,5,6,7]], axis=1)
oppPpg2022 = oppPpg2022.rename(columns={'2021': 'OppPPG'})

ppg2022 = ppg2022.drop(ppg2022.columns[[0,3,4,5,6,7]], axis=1)
ppg2022 = ppg2022.rename(columns={'2021': 'PPG'})

url = "https://www.teamrankings.com/ncaa-basketball/stat/points-per-game?date=2021-04-06"

html = requests.get(url).content
ppg2021_list = pd.read_html(html)
ppg2021 = ppg2021_list[0]

url = "https://www.teamrankings.com/ncaa-basketball/stat/opponent-points-per-game?date=2021-04-06"

html = requests.get(url).content
oppPpg2021_list = pd.read_html(html)
oppPpg2021 = oppPpg2021_list[0]


oppPpg2021 = oppPpg2021.drop(oppPpg2021.columns[[0,3,4,5,6,7]], axis=1)
oppPpg2021 = oppPpg2021.rename(columns={'2020': 'OppPPG'})

ppg2021 = ppg2021.drop(ppg2021.columns[[0,3,4,5,6,7]], axis=1)
ppg2021 = ppg2021.rename(columns={'2020': 'PPG'})

url = "https://www.teamrankings.com/ncaa-basketball/stat/points-per-game?date=2019-04-09"

html = requests.get(url).content
ppg2019_list = pd.read_html(html)
ppg2019 = ppg2019_list[0]

url = "https://www.teamrankings.com/ncaa-basketball/stat/points-per-game?date=2018-04-03"

html = requests.get(url).content
ppg2018_list = pd.read_html(html)
ppg2018 = ppg2018_list[0]

url = "https://en.wikipedia.org/wiki/2022_NCAA_Division_I_men%27s_basketball_tournament"

html = requests.get(url).content
MMteams_list = pd.read_html(html)

MMteams2022 = pd.DataFrame()
MMteams2022 = pd.concat([MMteams_list[5], MMteams_list[6], MMteams_list[7], MMteams_list[8]])
MMteams2022 = MMteams2022.reset_index(drop=True)

points2022 = ppg2022.merge(oppPpg2022)
points2022 = points2022.rename(columns={'Team': 'School'})
points2022['School'] = points2022['School'].apply(lambda x: x[:-2] + 'State' if x[-2:] == 'St' else x)


points2022.loc[154, 'School'] = 'New Mexico State'
points2022.loc[217, 'School'] = 'Cal State Fullerton'
points2022.loc[192, 'School'] = "Saint Mary's"
points2022.loc[18, 'School'] = "North Carolina"
points2022.loc[148, 'School'] = "Virginia Tech"
points2022.loc[274, 'School'] = "Saint Peter's"
points2022.loc[223, 'School'] = "TCU"
points2022.loc[110, 'School'] = "Loyola Chicago"
points2022.loc[1, 'School'] = "South Dakota State"
points2022.loc[158, 'School'] = "Jacksonville State"
points2022.loc[205, 'School'] = "Texas Southern"
points2022.loc[78, 'School'] = "Texas A&M–Corpus Christi"

MMteams2022 = pd.merge(MMteams2022, points2022)
MMteams2022['year'] = 2022

url = "https://en.wikipedia.org/wiki/2021_NCAA_Division_I_men%27s_basketball_tournament"

html = requests.get(url).content
MMteams_list = pd.read_html(html)

MMteams2021 = pd.DataFrame()
MMteams2021 = pd.concat([MMteams_list[4], MMteams_list[5], MMteams_list[6], MMteams_list[7]])
MMteams2021 = MMteams2021.reset_index(drop=True)

points2021 = ppg2021.merge(oppPpg2021)

points2021 = points2021.rename(columns={'Team': 'School'})

points2021['School'] = points2021['School'].apply(lambda x: x[:-2] + 'State' if x[-2:] == 'St' else x)

points2021.loc[90, 'School'] = 'UC Santa Barbara'
points2021.loc[23, 'School'] = 'Eastern Washington'
points2021.loc[192, 'School'] = "Grand Canyon"
points2021.loc[249, 'School'] = "Appalachian State"
points2021.loc[137, 'School'] = "UConn"
points2021.loc[179, 'School'] = "St. Bonaventure"
points2021.loc[103, 'School'] = "UNC Greensboro"
points2021.loc[81, 'School'] = "Abilene Christian"
points2021.loc[323, 'School'] = "Mount St. Mary's"
points2021.loc[107, 'School'] = "Texas Southern"
points2021.loc[58, 'School'] = "North Carolina"
points2021.loc[130, 'School'] = "Virginia Tech"
points2021.loc[30, 'School'] = "West Virginia"
points2021.loc[176, 'School'] = "Loyola Chicago"
points2021.loc[64, 'School'] = "Georgia Tech"

MMteams2021 = pd.merge(MMteams2021, points2021)
MMteams2021['year'] = 2021

MMteams = pd.concat([MMteams2022, MMteams2021], ignore_index=True)

MMteams['Conference'] = MMteams['Conference'].str.replace('Pac-12', 'Pac–12')
MMteams['Conference'] = MMteams['Conference'].str.replace('ASUN', 'Atlantic Sun')

n = 11
conference_counts = MMteams['Conference'].value_counts()
print(conference_counts)
top_conferences = conference_counts[:n].index.tolist()
MMteams.loc[~MMteams['Conference'].isin(top_conferences), 'Conference'] = 'Other'
conference_counts = MMteams['Conference'].value_counts()

plt.figure(figsize=(8,8))
plt.pie(conference_counts, labels=conference_counts.index, autopct='%1.1f%%')
plt.title('Conference Distribution')
plt.show()