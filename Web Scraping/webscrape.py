import requests
import pandas as pd
import numpy as np

url = "https://www.teamrankings.com/ncaa-basketball/stat/points-per-game?date=2022-04-05"

html = requests.get(url).content
ppg2022_list = pd.read_html(html)
ppg2022 = ppg2022_list[0]

url = "https://www.teamrankings.com/ncaa-basketball/stat/opponent-points-per-game?date=2022-04-05"

html = requests.get(url).content
oppPpg2022_list = pd.read_html(html)
oppPpg2022 = oppPpg2022_list[0]

ppg2022 = ppg2022.drop(ppg2022.columns[[0,3,4,5,6,7]], axis=1)
oppPpg2022 = oppPpg2022.drop(oppPpg2022.columns[[0,3,4,5,6,7]], axis=1)

ppg2022 = ppg2022.rename(columns={'2021': 'PPG'})
oppPpg2022 = oppPpg2022.rename(columns={'2021': 'OppPPG'})


stats_2022 = ppg2022.merge(oppPpg2022)

astats_2022 = []

Gonzaga2022 = stats_2022[stats_2022['Team'] == 'Gonzaga']
GeorgiaSt2022 = stats_2022[stats_2022['Team'] == 'Georgia St'].reset_index(drop=True)
vsGeorgiaSt2022 = GeorgiaSt2022.rename(columns = lambda x: 'vs' + x).reset_index(drop=True)
vsGonzaga2022 = Gonzaga2022.rename(columns = lambda x: 'vs' + x).reset_index(drop=True)
BoiseSt2022 = stats_2022[stats_2022['Team'] == 'Boise State'].reset_index(drop=True)
Memphis2022 = stats_2022[stats_2022['Team'] == 'Memphis'].reset_index(drop=True)
vsBoiseSt2022 = BoiseSt2022.rename(columns = lambda x: 'vs' + x).reset_index(drop=True)
vsMemphis2022 = Memphis2022.rename(columns = lambda x: 'vs' + x).reset_index(drop=True)


astats_2022 = pd.concat([Gonzaga2022, vsGeorgiaSt2022], axis=1)
astats_2022.loc[len(astats_2022)] = pd.concat([GeorgiaSt2022, vsGonzaga2022], axis=1).iloc[0]
astats_2022.loc[len(astats_2022)] = pd.concat([Memphis2022, vsBoiseSt2022], axis=1).iloc[0]
astats_2022.loc[len(astats_2022)] = pd.concat([BoiseSt2022, vsMemphis2022], axis=1).iloc[0]

astats_2022.loc[0::2, 'Win'] = 1
astats_2022.loc[1::2, 'Win'] = 0

astats_2022