import pandas as pd
import requests

url = "https://www.teamrankings.com/ncaa-basketball/stat/points-per-game?date=2022-04-05"

html = requests.get(url).content
ppg2022_list = pd.read_html(html)
ppg2022 = ppg2022_list[0]


ppg2022 = ppg2022.drop(ppg2022.columns[[0,3,4,5,6,7]], axis=1)

ppg2022 = ppg2022.rename(columns={'2021': 'PPG'})

url = "https://en.wikipedia.org/wiki/2022_NCAA_Division_I_men%27s_basketball_tournament"

html = requests.get(url).content
MMteams_list = pd.read_html(html)

ppg2022_edited = pd.DataFrame()
MMteams2022 = pd.DataFrame()
MMteams2022 = pd.concat([MMteams_list[5], MMteams_list[6], MMteams_list[7], MMteams_list[8]])
MMteams2022 = MMteams2022.reset_index(drop=True)
ppg2022 = ppg2022.rename(columns={'Team': 'School'})

ppg2022['School'] = ppg2022['School'].apply(lambda x: x[:-2] + 'State' if x[-2:] == 'St' else x)


ppg2022.loc[154, 'School'] = 'New Mexico State'
ppg2022.loc[217, 'School'] = 'Cal State Fullerton'
ppg2022.loc[192, 'School'] = "Saint Mary's"
ppg2022.loc[18, 'School'] = "North Carolina"
ppg2022.loc[148, 'School'] = "Virginia Tech"
ppg2022.loc[274, 'School'] = "Saint Peter's"
ppg2022.loc[223, 'School'] = "TCU"
ppg2022.loc[110, 'School'] = "Loyola Chicago"
ppg2022.loc[1, 'School'] = "South Dakota State"
ppg2022.loc[158, 'School'] = "Jacksonville State"

ppg2022.loc[205, 'School'] = "Texas Southern"
ppg2022.loc[78, 'School'] = "Texas A&M–Corpus Christi"

MMteams2022 = pd.merge(MMteams2022, ppg2022)
MMteams2022

import matplotlib.pyplot as plt

n = 10
conference_counts = MMteams2022['Conference'].value_counts()
top_conferences = conference_counts[:n].index.tolist()
MMteams2022.loc[~MMteams2022['Conference'].isin(top_conferences), 'Conference'] = 'Other'
conference_counts = MMteams2022['Conference'].value_counts()

plt.figure(figsize=(8,8))
plt.pie(conference_counts, labels=conference_counts.index, autopct='%1.1f%%')
plt.title('Conference Distribution')
plt.show()