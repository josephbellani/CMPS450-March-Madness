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

url = "https://www.teamrankings.com/ncaa-basketball/stat/opponent-points-per-game?date=2019-04-09"

html = requests.get(url).content
oppPpg2019_list = pd.read_html(html)
oppPpg2019 = oppPpg2019_list[0]


oppPpg2019 = oppPpg2019.drop(oppPpg2019.columns[[0,3,4,5,6,7]], axis=1)
oppPpg2019 = oppPpg2019.rename(columns={'2018': 'OppPPG'})

ppg2019 = ppg2019.drop(ppg2019.columns[[0,3,4,5,6,7]], axis=1)
ppg2019 = ppg2019.rename(columns={'2018': 'PPG'})

url = "https://www.teamrankings.com/ncaa-basketball/stat/points-per-game?date=2018-04-03"

html = requests.get(url).content
ppg2018_list = pd.read_html(html)
ppg2018 = ppg2018_list[0]

url = "https://www.teamrankings.com/ncaa-basketball/stat/opponent-points-per-game?date=2018-04-03"

html = requests.get(url).content
oppPpg2018_list = pd.read_html(html)
oppPpg2018 = oppPpg2018_list[0]


oppPpg2018 = oppPpg2018.drop(oppPpg2018.columns[[0,3,4,5,6,7]], axis=1)
oppPpg2018 = oppPpg2018.rename(columns={'2017': 'OppPPG'})

ppg2018 = ppg2018.drop(ppg2018.columns[[0,3,4,5,6,7]], axis=1)
ppg2018 = ppg2018.rename(columns={'2017': 'PPG'})

url = "https://www.teamrankings.com/ncaa-basketball/stat/points-per-game?date=2017-04-04"

html = requests.get(url).content
ppg2017_list = pd.read_html(html)
ppg2017 = ppg2017_list[0]

url = "https://www.teamrankings.com/ncaa-basketball/stat/opponent-points-per-game?date=2017-04-04"

html = requests.get(url).content
oppPpg2017_list = pd.read_html(html)
oppPpg2017 = oppPpg2017_list[0]


oppPpg2017 = oppPpg2017.drop(oppPpg2017.columns[[0,3,4,5,6,7]], axis=1)
oppPpg2017 = oppPpg2017.rename(columns={'2016': 'OppPPG'})

ppg2017 = ppg2017.drop(ppg2017.columns[[0,3,4,5,6,7]], axis=1)
ppg2017 = ppg2017.rename(columns={'2016': 'PPG'})

url = "https://www.teamrankings.com/ncaa-basketball/stat/points-per-game?date=2016-04-05"

html = requests.get(url).content
ppg2016_list = pd.read_html(html)
ppg2016 = ppg2016_list[0]

url = "https://www.teamrankings.com/ncaa-basketball/stat/opponent-points-per-game?date=2016-04-05"

html = requests.get(url).content
oppPpg2016_list = pd.read_html(html)
oppPpg2016 = oppPpg2016_list[0]


oppPpg2016 = oppPpg2016.drop(oppPpg2016.columns[[0,3,4,5,6,7]], axis=1)
oppPpg2016 = oppPpg2016.rename(columns={'2015': 'OppPPG'})

ppg2016 = ppg2016.drop(ppg2016.columns[[0,3,4,5,6,7]], axis=1)
ppg2016 = ppg2016.rename(columns={'2015': 'PPG'})

url = "https://www.teamrankings.com/ncaa-basketball/stat/points-per-game?date=2015-04-06"

html = requests.get(url).content
ppg2015_list = pd.read_html(html)
ppg2015 = ppg2015_list[0]

url = "https://www.teamrankings.com/ncaa-basketball/stat/opponent-points-per-game?date=2015-04-06"

html = requests.get(url).content
oppPpg2015_list = pd.read_html(html)
oppPpg2015 = oppPpg2015_list[0]


oppPpg2015 = oppPpg2015.drop(oppPpg2015.columns[[0,3,4,5,6,7]], axis=1)
oppPpg2015 = oppPpg2015.rename(columns={'2014': 'OppPPG'})

ppg2015 = ppg2015.drop(ppg2015.columns[[0,3,4,5,6,7]], axis=1)
ppg2015 = ppg2015.rename(columns={'2014': 'PPG'})

url = "https://www.teamrankings.com/ncaa-basketball/stat/points-per-game?date=2014-04-07"

html = requests.get(url).content
ppg2014_list = pd.read_html(html)
ppg2014 = ppg2014_list[0]

url = "https://www.teamrankings.com/ncaa-basketball/stat/opponent-points-per-game?date=2014-04-07"

html = requests.get(url).content
oppPpg2014_list = pd.read_html(html)
oppPpg2014 = oppPpg2014_list[0]


oppPpg2014 = oppPpg2014.drop(oppPpg2014.columns[[0,3,4,5,6,7]], axis=1)
oppPpg2014 = oppPpg2014.rename(columns={'2013': 'OppPPG'})

ppg2014 = ppg2014.drop(ppg2014.columns[[0,3,4,5,6,7]], axis=1)
ppg2014 = ppg2014.rename(columns={'2013': 'PPG'})

url = "https://www.teamrankings.com/ncaa-basketball/stat/points-per-game?date=2013-04-08"

html = requests.get(url).content
ppg2013_list = pd.read_html(html)
ppg2013 = ppg2013_list[0]

url = "https://www.teamrankings.com/ncaa-basketball/stat/opponent-points-per-game?date=2013-04-08"

html = requests.get(url).content
oppPpg2013_list = pd.read_html(html)
oppPpg2013 = oppPpg2013_list[0]


oppPpg2013 = oppPpg2013.drop(oppPpg2013.columns[[0,3,4,5,6,7]], axis=1)
oppPpg2013 = oppPpg2013.rename(columns={'2012': 'OppPPG'})

ppg2013 = ppg2013.drop(ppg2013.columns[[0,3,4,5,6,7]], axis=1)
ppg2013 = ppg2013.rename(columns={'2012': 'PPG'})

url = "https://www.teamrankings.com/ncaa-basketball/stat/points-per-game?date=2012-04-02"

html = requests.get(url).content
ppg2012_list = pd.read_html(html)
ppg2012 = ppg2012_list[0]

url = "https://www.teamrankings.com/ncaa-basketball/stat/opponent-points-per-game?date=2012-04-02"

html = requests.get(url).content
oppPpg2012_list = pd.read_html(html)
oppPpg2012 = oppPpg2012_list[0]

oppPpg2012 = oppPpg2012.drop(oppPpg2012.columns[[0,3,4,5,6,7]], axis=1)
oppPpg2012 = oppPpg2012.rename(columns={'2011': 'OppPPG'})

ppg2012 = ppg2012.drop(ppg2012.columns[[0,3,4,5,6,7]], axis=1)
ppg2012 = ppg2012.rename(columns={'2011': 'PPG'})

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

url = "https://en.wikipedia.org/wiki/2019_NCAA_Division_I_men%27s_basketball_tournament"

html = requests.get(url).content
MMteams_list = pd.read_html(html)

MMteams2019 = pd.DataFrame()
MMteams2019 = pd.concat([MMteams_list[4], MMteams_list[5], MMteams_list[6], MMteams_list[7]])
MMteams2019 = MMteams2019.reset_index(drop=True)

points2019 = ppg2019.merge(oppPpg2019)

points2019 = points2019.rename(columns={'Team': 'School'})

points2019['School'] = points2019['School'].apply(lambda x: x[:-2] + 'State' if x[-2:] == 'St' else x)

points2019.loc[125, 'School'] = "Virginia Tech"
points2019.loc[50, 'School'] = 'Mississippi State'
points2019.loc[150, 'School'] = 'UCF'
points2019.loc[276, 'School'] = "North Carolina Central"
points2019.loc[154, 'School'] = "North Dakota State"
points2019.loc[53, 'School'] = "St. John's"
points2019.loc[52, 'School'] = "Northern Kentucky"
points2019.loc[102, 'School'] = "Fairleigh Dickinson"
points2019.loc[90, 'School'] = "Prairie View A&M"
points2019.loc[81, 'School'] = "Ole Miss"
points2019.loc[147, 'School'] = "Saint Mary's"
points2019.loc[86, 'School'] = "Gardner–Webb"
points2019.loc[2, 'School'] = "North Carolina"
points2019.loc[45, 'School'] = "New Mexico State"
points2019.loc[78, 'School'] = "Northeastern"
points2019.loc[207, 'School'] = "Abilene Christian"

MMteams2019 = pd.merge(MMteams2019, points2019)
MMteams2019['year'] = 2019

url = "https://en.wikipedia.org/wiki/2018_NCAA_Division_I_men%27s_basketball_tournament"

html = requests.get(url).content
MMteams_list = pd.read_html(html)

MMteams2018 = pd.DataFrame()
MMteams2018 = pd.concat([MMteams_list[3], MMteams_list[4], MMteams_list[5], MMteams_list[6]])
MMteams2018 = MMteams2018.reset_index(drop=True)

points2018 = ppg2018.merge(oppPpg2018)

points2018 = points2018.rename(columns={'Team': 'School'})

points2018['School'] = points2018['School'].apply(lambda x: x[:-2] + 'State' if x[-2:] == 'St' else x)

points2018.loc[231, 'School'] = "Loyola Chicago"
points2018.loc[216, 'School'] = "UMBC"
points2018.loc[21, 'School'] = 'North Carolina'
points2018.loc[11, 'School'] = "South Dakota State"
points2018.loc[208, 'School'] = "UNC Greensboro"
points2018.loc[253, 'School'] = "North Carolina Central"
points2018.loc[64, 'School'] = "Texas Southern"
points2018.loc[36, 'School'] = "West Virginia"
points2018.loc[38, 'School'] = "Virginia Tech"
points2018.loc[70, 'School'] = "St. Bonaventure"
points2018.loc[62, 'School'] = "Stephen F. Austin"
points2018.loc[211, 'School'] = "Cal State Fullerton"
points2018.loc[83, 'School'] = "LIU Brooklyn"
points2018.loc[17, 'School'] = "TCU"
points2018.loc[105, 'School'] = "New Mexico State"
points2018.loc[122, 'School'] = "College of Charleston"
points2018.loc[109, 'School'] = "Penn"

MMteams2018 = pd.merge(MMteams2018, points2018)
MMteams2018['year'] = 2018

url = "https://en.wikipedia.org/wiki/2017_NCAA_Division_I_men%27s_basketball_tournament"

html = requests.get(url).content
MMteams_list = pd.read_html(html)

MMteams2017 = pd.DataFrame()
MMteams2017 = pd.concat([MMteams_list[3], MMteams_list[4], MMteams_list[5], MMteams_list[6]])
MMteams2017 = MMteams2017.reset_index(drop=True)

points2017 = ppg2017.merge(oppPpg2017)

points2017 = points2017.rename(columns={'Team': 'School'})

points2017['School'] = points2017['School'].apply(lambda x: x[:-2] + 'State' if x[-2:] == 'St' else x)

points2017.loc[130, 'School'] = "SMU"
points2017.loc[170, 'School'] = "South Carolina"
points2017.loc[39, 'School'] = 'Virginia Tech'
points2017.loc[13, 'School'] = "UNC Wilmington"
points2017.loc[37, 'School'] = "East Tennessee State"
points2017.loc[62, 'School'] = "New Mexico State"
points2017.loc[284, 'School'] = "Mount St. Mary's"
points2017.loc[329, 'School'] = "Jacksonville State"
points2017.loc[165, 'School'] = "North Carolina Central"
points2017.loc[18, 'School'] = "West Virginia"
points2017.loc[187, 'School'] = "Saint Mary's"
points2017.loc[77, 'School'] = "Florida Gulf Coast"
points2017.loc[85, 'School'] = "South Dakota State"
points2017.loc[8, 'School'] = "North Carolina"
points2017.loc[135, 'School'] = "Middle Tennessee"
points2017.loc[120, 'School'] = "Northern Kentucky"
points2017.loc[136, 'School'] = "Texas Southern"

MMteams2017 = pd.merge(MMteams2017, points2017)
MMteams2017['year'] = 2017

url = "https://en.wikipedia.org/wiki/2016_NCAA_Division_I_men%27s_basketball_tournament"

html = requests.get(url).content
MMteams_list = pd.read_html(html)

MMteams2016 = pd.DataFrame()
MMteams2016 = pd.concat([MMteams_list[3], MMteams_list[4], MMteams_list[5], MMteams_list[6]])
MMteams2016 = MMteams2016.reset_index(drop=True)

points2016 = ppg2016.merge(oppPpg2016)

points2016 = points2016.rename(columns={'Team': 'School'})

points2016['School'] = points2016['School'].apply(lambda x: x[:-2] + 'State' if x[-2:] == 'St' else x)

points2016.loc[102, 'School'] = "Miami"
points2016.loc[157, 'School'] = "UConn"
points2016.loc[96, 'School'] = 'South Dakota State'
points2016.loc[137, 'School'] = "UNC Asheville"
points2016.loc[61, 'School'] = "Saint Joseph's"
points2016.loc[266, 'School'] = "Northern Iowa"
points2016.loc[41, 'School'] = "UNC Wilmington"
points2016.loc[8, 'School'] = "Green Bay"
points2016.loc[187, 'School'] = "Cal State Bakersfield"
points2016.loc[7, 'School'] = "North Carolina"
points2016.loc[35, 'School'] = "West Virginia"
points2016.loc[28, 'School'] = "Stephen F. Austin"
points2016.loc[86, 'School'] = "Florida Gulf Coast"
points2016.loc[74, 'School'] = "Fairleigh Dickinson"
points2016.loc[232, 'School'] = "Little Rock"
points2016.loc[177, 'School'] = "Middle Tennessee"

MMteams2016 = pd.merge(MMteams2016, points2016)
MMteams2016['year'] = 2016

url = "https://en.wikipedia.org/wiki/2015_NCAA_Division_I_men%27s_basketball_tournament"

html = requests.get(url).content
MMteams_list = pd.read_html(html)

MMteams2015 = pd.DataFrame()
MMteams2015 = pd.concat([MMteams_list[3], MMteams_list[4], MMteams_list[5], MMteams_list[6]])
MMteams2015 = MMteams2015.reset_index(drop=True)

points2015 = ppg2015.merge(oppPpg2015)

points2015 = points2015.rename(columns={'Team': 'School'})

points2015['School'] = points2015['School'].apply(lambda x: x[:-2] + 'State' if x[-2:] == 'St' else x)

points2015.loc[42, 'School'] = "West Virginia"
points2015.loc[125, 'School'] = "Northeastern"
points2015.loc[156, 'School'] = 'New Mexico State'
points2015.loc[12, 'School'] = "North Carolina"
points2015.loc[133, 'School'] = "Texas Southern"
points2015.loc[71, 'School'] = "Coastal Carolina"
points2015.loc[218, 'School'] = "Northern Iowa"
points2015.loc[78, 'School'] = "North Carolina State"
points2015.loc[105, 'School'] = "SMU"
points2015.loc[74, 'School'] = "St. John's"
points2015.loc[7, 'School'] = "Stephen F. Austin"
points2015.loc[4, 'School'] = "Eastern Washington"
points2015.loc[235, 'School'] = "North Dakota State"
points2015.loc[28, 'School'] = "North Florida"
points2015.loc[111, 'School'] = "Robert Morris"

MMteams2015 = pd.merge(MMteams2015, points2015)
MMteams2015['year'] = 2015

url = "https://en.wikipedia.org/wiki/2014_NCAA_Division_I_men%27s_basketball_tournament"

html = requests.get(url).content
MMteams_list = pd.read_html(html)

MMteams2014 = pd.DataFrame()
MMteams2014 = pd.concat([MMteams_list[4], MMteams_list[5], MMteams_list[6], MMteams_list[7]])
MMteams2014 = MMteams2014.reset_index(drop=True)

points2014 = ppg2014.merge(oppPpg2014)

points2014 = points2014.rename(columns={'Team': 'School'})

points2014['School'] = points2014['School'].apply(lambda x: x[:-2] + 'State' if x[-2:] == 'St' else x)

points2014.loc[50, 'School'] = "Stephen F. Austin"
points2014.loc[128, 'School'] = "Western Michigan"
points2014.loc[156, 'School'] = 'Eastern Kentucky'
points2014.loc[42, 'School'] = "Mount St. Mary's"
points2014.loc[35, 'School'] = "North Carolina"
points2014.loc[113, 'School'] = "UConn"
points2014.loc[85, 'School'] = "George Washington"
points2014.loc[129, 'School'] = "Saint Joseph's"
points2014.loc[106, 'School'] = "North Carolina Central"
points2014.loc[178, 'School'] = "Milwaukee"
points2014.loc[170, 'School'] = "Coastal Carolina"
points2014.loc[72, 'School'] = "North Dakota State"
points2014.loc[36, 'School'] = "New Mexico State"
points2014.loc[15, 'School'] = "Louisiana-Lafayette"
points2014.loc[60, 'School'] = "Texas Southern"
points2014.loc[44, 'School'] = "Massachusetts"

MMteams2014 = pd.merge(MMteams2014, points2014)
MMteams2014['year'] = 2014

url = "https://en.wikipedia.org/wiki/2013_NCAA_Division_I_men%27s_basketball_tournament"

html = requests.get(url).content
MMteams_list = pd.read_html(html, header=0)

MMteams2013 = pd.DataFrame()
MMteams2013 = pd.concat([MMteams_list[3], MMteams_list[4],MMteams_list[5], MMteams_list[6]])
MMteams2013 = MMteams2013.reset_index(drop=True)

points2013 = ppg2013.merge(oppPpg2013)

points2013 = points2013.rename(columns={'Team': 'School'})

points2013['School'] = points2013['School'].apply(lambda x: x[:-2] + 'State' if x[-2:] == 'St' else x)

points2013.loc[15, 'School'] = "North Carolina"
points2013.loc[49, 'School'] = "South Dakota State"
points2013.loc[9, 'School'] = 'Northwestern State'
points2013.loc[51, 'School'] = "Florida Gulf Coast"
points2013.loc[177, 'School'] = "Western Kentucky"
points2013.loc[6, 'School'] = "Ole Miss"
points2013.loc[106, 'School'] = "Miami"
points2013.loc[215, 'School'] = "James Madison"
points2013.loc[2, 'School'] = "Long Island"
points2013.loc[78, 'School'] = "Middle Tennessee"
points2013.loc[29, 'School'] = "Saint Mary's (CA)"
points2013.loc[163, 'School'] = "New Mexico State"
points2013.loc[288, 'School'] = "North Carolina A&T"

MMteams2013 = pd.merge(MMteams2013, points2013)
MMteams2013['year'] = 2013
url = "https://en.wikipedia.org/wiki/2012_NCAA_Division_I_men%27s_basketball_tournament"

html = requests.get(url).content
MMteams_list = pd.read_html(html)

MMteams2012 = pd.DataFrame()
MMteams_list[4].columns = ['Seed', 'School', 'Conference', 'Record', 'Berth type', 'Overall rank']
MMteams_list[5].columns = ['Seed', 'School', 'Conference', 'Record', 'Berth type', 'Overall rank']
MMteams_list[6].columns = ['Seed', 'School', 'Conference', 'Record', 'Berth type', 'Overall rank']
MMteams_list[7].columns = ['Seed', 'School', 'Conference', 'Record', 'Berth type', 'Overall rank']
MMteams2012 = pd.concat([MMteams_list[4],MMteams_list[5], MMteams_list[6], MMteams_list[7]])
MMteams2012 = MMteams2012.reset_index(drop=True)

points2012 = ppg2012.merge(oppPpg2012)

points2012 = points2012.rename(columns={'Team': 'School'})

points2012['School'] = points2012['School'].apply(lambda x: x[:-2] + 'State' if x[-2:] == 'St' else x)

points2012.loc[94, 'School'] = "Southern Miss"
points2012.loc[85, 'School'] = "West Virginia"
points2012.loc[96, 'School'] = 'St. Bonaventure'
points2012.loc[171, 'School'] = "Loyola"
points2012.loc[8, 'School'] = "UNC Asheville"
points2012.loc[2, 'School'] = "North Carolina"
points2012.loc[42, 'School'] = "Saint Mary's"
points2012.loc[324, 'School'] = "South Florida"
points2012.loc[100, 'School'] = "Detroit Mercy"
points2012.loc[13, 'School'] = "New Mexico State"
points2012.loc[141, 'School'] = "Mississippi Valley State"
points2012.loc[233, 'School'] = "Western Kentucky"
points2012.loc[43, 'School'] = "Long Beach State"
points2012.loc[22, 'School'] = "South Dakota State"

MMteams2012 = pd.merge(MMteams2012, points2012)
MMteams2012['year'] = 2012

MMteams = pd.concat([MMteams2022, MMteams2021, MMteams2019, MMteams2018, MMteams2017, MMteams2016, MMteams2015, MMteams2014, MMteams2013, MMteams2012], ignore_index=True)

MMteams['Overall Seed'] = MMteams['Overall rank'].combine_first(MMteams['Overall Seed'])
MMteams['Overall Seed'] = MMteams['Overall rank[4]'].combine_first(MMteams['Overall Seed'])
MMteams = MMteams.drop(['Overall rank', 'Coach', 'Overall rank[4]'], axis=1)


MMteams['Conference'] = MMteams['Conference'].str.replace('Pac-12', 'Pac–12')
MMteams['Conference'] = MMteams['Conference'].str.replace('ASUN', 'Atlantic Sun')
MMteams['Conference'] = MMteams['Conference'].str.replace('CAA', 'Colonial')
MMteams['Conference'] = MMteams['Conference'].str.replace('Ivy League', 'Ivy')
MMteams['Conference'] = MMteams['Conference'].str.replace('WCC', 'West Coast')
MMteams['Conference'] = MMteams['Conference'].str.replace('Summit League', 'Summit')
MMteams['Conference'] = MMteams['Conference'].str.replace('Conference USA', 'C-USA')
MMteams['Conference'] = MMteams['Conference'].str.replace('NEC', 'Northeast')
MMteams['Conference'] = MMteams['Conference'].str.replace('Mid American', 'MAC')
MMteams['Conference'] = MMteams['Conference'].str.replace('MVC', 'Missouri Valley')

n = 15
conference_counts = MMteams['Conference'].value_counts()
print(conference_counts)
top_conferences = conference_counts[:n].index.tolist()
MMteams.loc[~MMteams['Conference'].isin(top_conferences), 'Conference'] = '1 Bid Conferences'
conference_counts = MMteams['Conference'].value_counts()

plt.figure(figsize=(8,8))
plt.pie(conference_counts, labels=conference_counts.index, autopct='%1.1f%%')
plt.title('Conference Distribution')
plt.show()

MMteams['PPG'] = MMteams['PPG'].astype(float)
MMteams['OppPPG'] = MMteams['OppPPG'].astype(float)


grouped = MMteams.groupby('year')[['PPG', 'OppPPG']].mean()

grouped.plot(kind='bar', width=0.8, figsize=(8, 6))
plt.xlabel('Year')
plt.ylabel('Points per game')
plt.title('Average PPG and OppPPG by year')
plt.legend(['PPG', 'OppPPG'])
plt.show()

MMteams['Seed'] = MMteams['Seed'].astype(str)

MMteams['Seed'] = MMteams['Seed'].str.replace('*', '')
MMteams['Seed'] = MMteams['Seed'].str.replace('#', '')

MMteams['Seed'] = MMteams['Seed'].astype(float)

avg_seed = MMteams.groupby('Conference')['Seed'].mean()
avg_seed_sorted = avg_seed.sort_values(ascending=False)

fig, ax = plt.subplots(figsize=(10, 10))

ax.barh(avg_seed_sorted.index, avg_seed_sorted.values)

ax.set_title('Average Seed by Conference')
ax.set_xlabel('Conference')
ax.set_ylabel('Average Seed')
ax.tick_params(axis='x', rotation=10)
plt.show()