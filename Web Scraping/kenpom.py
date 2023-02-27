import pandas as pd
import requests

MMteams = pd.read_csv('MMteams.csv')

# Reads in data from kenpom2022, as well as renaming and dropping certain columns and cleaning data
kenpom2022 = pd.read_csv('kenpom2022.csv')
kenpom2022 = kenpom2022.rename(columns={'Team': 'School', 'AdjEM.1': 'SOS AdjEM'})
kenpom2022['year'] = 2022
kenpom2022 = kenpom2022.drop(['W-L', 'Conference'], axis=1)
kenpom2022['School'] = kenpom2022['School'].str.replace(' \d+', '')

# Reads in data from kenpom2021, as well as renaming and dropping certain columns and cleaning data
kenpom2021 = pd.read_csv('kenpom2021.csv')
kenpom2021 = kenpom2021.rename(columns={'Team': 'School', 'AdjEM.1': 'SOS AdjEM'})
kenpom2021['year'] = 2021
kenpom2021 = kenpom2021.drop(['W-L', 'Conference'], axis=1)
kenpom2021['School'] = kenpom2021['School'].str.replace(' \d+', '')

# Reads in data from kenpom2019, as well as renaming and dropping certain columns and cleaning data
kenpom2019 = pd.read_csv('kenpom2019.csv')
kenpom2019 = kenpom2019.rename(columns={'Team': 'School', 'AdjEM.1': 'SOS AdjEM'})
kenpom2019['year'] = 2019
kenpom2019 = kenpom2019.drop(['W-L', 'Conference'], axis=1)
kenpom2019['School'] = kenpom2019['School'].str.replace(' \d+', '')

# Reads in data from kenpom2018, as well as renaming and dropping certain columns and cleaning data
kenpom2018 = pd.read_csv('kenpom2018.csv')
kenpom2018 = kenpom2018.rename(columns={'Team': 'School', 'AdjEM.1': 'SOS AdjEM'})
kenpom2018['year'] = 2018
kenpom2018 = kenpom2018.drop(['W-L', 'Conference'], axis=1)
kenpom2018['School'] = kenpom2018['School'].str.replace(' \d+', '')

# Reads in data from kenpom2017, as well as renaming and dropping certain columns and cleaning data
kenpom2017 = pd.read_csv('kenpom2017.csv')
kenpom2017 = kenpom2017.rename(columns={'Team': 'School', 'AdjEM.1': 'SOS AdjEM'})
kenpom2017['year'] = 2017
kenpom2017 = kenpom2017.drop(['W-L', 'Conference'], axis=1)
kenpom2017['School'] = kenpom2017['School'].str.replace(' \d+', '')

# Reads in data from kenpom2016, as well as renaming and dropping certain columns and cleaning data
kenpom2016 = pd.read_csv('kenpom2016.csv')
kenpom2016 = kenpom2016.rename(columns={'Team': 'School', 'AdjEM.1': 'SOS AdjEM'})
kenpom2016['year'] = 2016
kenpom2016 = kenpom2016.drop(['W-L', 'Conference'], axis=1)
kenpom2016['School'] = kenpom2016['School'].str.replace(' \d+', '')

# Reads in data from kenpom2015, as well as renaming and dropping certain columns and cleaning data
kenpom2015 = pd.read_csv('kenpom2015.csv')
kenpom2015 = kenpom2015.rename(columns={'Team': 'School', 'AdjEM.1': 'SOS AdjEM'})
kenpom2015['year'] = 2015
kenpom2015 = kenpom2015.drop(['W-L', 'Conference'], axis=1)
kenpom2015['School'] = kenpom2015['School'].str.replace(' \d+', '')

# Reads in data from kenpom2014, as well as renaming and dropping certain columns and cleaning data
kenpom2014 = pd.read_csv('kenpom2014.csv')
kenpom2014 = kenpom2014.rename(columns={'Team': 'School', 'AdjEM.1': 'SOS AdjEM'})
kenpom2014['year'] = 2014
kenpom2014 = kenpom2014.drop(['W-L', 'Conference'], axis=1)
kenpom2014['School'] = kenpom2014['School'].str.replace(' \d+', '')

# Reads in data from kenpom2013, as well as renaming and dropping certain columns and cleaning data
kenpom2013 = pd.read_csv('kenpom2013.csv')
kenpom2013 = kenpom2013.rename(columns={'Team': 'School', 'AdjEM.1': 'SOS AdjEM'})
kenpom2013['year'] = 2013
kenpom2013 = kenpom2013.drop(['W-L', 'Conference'], axis=1)
kenpom2013['School'] = kenpom2013['School'].str.replace(' \d+', '')

# Reads in data from kenpom2012, as well as renaming and dropping certain columns and cleaning data
kenpom2012 = pd.read_csv('kenpom2012.csv')
kenpom2012 = kenpom2012.rename(columns={'Team': 'School', 'AdjEM.1': 'SOS AdjEM'})
kenpom2012['year'] = 2012
kenpom2012 = kenpom2012.drop(['W-L', 'Conference'], axis=1)
kenpom2012['School'] = kenpom2012['School'].str.replace(' \d+', '')

# Concatenates every kenpom csv from 2012-2022
kenpom = pd.concat([kenpom2022, kenpom2021, kenpom2019, kenpom2018, kenpom2017, kenpom2016, kenpom2015, kenpom2014, kenpom2013, kenpom2012], ignore_index=True)

# Renames school that had 2 different names in the MMteams dataframe
MMteams['School'] = MMteams['School'].str.replace(r'^Miami$', 'Miami (FL)', regex=True)
MMteams['School'] = MMteams['School'].str.replace('North Carolina State', 'NC State')
MMteams['School'] = MMteams['School'].str.replace('Connecticut', 'UConn')
MMteams['School'] = MMteams['School'].str.replace(r'\bMississippi\b', 'Ole Miss', regex=True)
MMteams['School'] = MMteams['School'].str.replace("Saint Mary's \(CA\)", "Saint Mary's")
MMteams['School'] = MMteams['School'].str.replace("Long Island", "LIU-Brooklyn")
MMteams['School'] = MMteams['School'].str.replace("LIU Brooklyn", "LIU-Brooklyn")

# Renames schools that differed from the names in the MMteams Dataframe
kenpom['School'] = kenpom['School'].apply(lambda x: x[:-3] + 'State' if x[-3:] == 'St.' else x)
kenpom['School'] = kenpom['School'].str.replace('Cal St. Fullerton', 'Cal State Fullerton')
kenpom['School'] = kenpom['School'].str.replace('Miami FL', 'Miami (FL)')
kenpom['School'] = kenpom['School'].str.replace('Texas A&M Corpus Chris', 'Texas A&M–Corpus Christi')
kenpom['School'] = kenpom['School'].str.replace('Connecticut', 'UConn')
kenpom['School'] = kenpom['School'].str.replace('Mississippi', 'Ole Miss')
kenpom['School'] = kenpom['School'].str.replace('N.C. State', 'NC State')
kenpom['School'] = kenpom['School'].str.replace('Gardner Webb', 'Gardner–Webb')
kenpom['School'] = kenpom['School'].str.replace('Cal St. Bakersfield', 'Cal State Bakersfield')
kenpom['School'] = kenpom['School'].str.replace('Arkansas Little Rock', 'Little Rock')
kenpom['School'] = kenpom['School'].str.replace('Loyola MD', 'Loyola')
kenpom['School'] = kenpom['School'].str.replace('Detroit', 'Detroit Mercy')
kenpom['School'] = kenpom['School'].str.replace('LIU Brooklyn', 'LIU-Brooklyn')
kenpom['School'] = kenpom['School'].str.replace('Louisiana Lafayette', 'Louisiana-Lafayette')

# Reads in website used to get the State each school is located in
url = "https://en.wikipedia.org/wiki/List_of_NCAA_Division_I_institutions"

html = requests.get(url).content
MMteams_list = pd.read_html(html)

MMstates = pd.DataFrame()
MMstates = MMteams_list[1]

# Drops the unnecessary columns, and renames the team name to 'School'
MMstates = MMstates.drop(['School Name', 'Teams', 'Location', 'Type', 'Subdivision', 'Primary Conference'], axis = 1)
MMstates = MMstates.rename(columns={'Common Name': 'School'})

# Merges MMteams and kenpom
stats = pd.merge(MMteams, kenpom, how='inner', on=['School', 'year'])

# Renames schools that got overwritten previously
stats['School'] = stats['School'].str.replace('Ole Miss State', 'Mississippi State')
stats['School'] = stats['School'].str.replace('Ole Miss Valley State', 'Mississippi Valley State')

# Renames schools from MMstates to match stats
MMstates['School'] = MMstates['School'].str.replace("USC\[an\]", 'USC')
MMstates['School'] = MMstates['School'].str.replace("Miami \(Florida\)", 'Miami (FL)')
MMstates['School'] = MMstates['School'].str.replace("LIU", 'LIU-Brooklyn')
MMstates['School'] = MMstates['School'].str.replace("Charleston\[g\]", 'College of Charleston')
MMstates['School'] = MMstates['School'].str.replace("FGCU", 'Florida Gulf Coast')
MMstates['School'] = MMstates['School'].str.replace("Hawaiʻi", 'Hawaii')
MMstates['School'] = MMstates['School'].str.replace("Louisiana", 'Louisiana-Lafayette')
MMstates['School'] = MMstates['School'].str.replace("UMass", 'Massachusetts')

# Merges stats and MMstates
fullstats = pd.merge(stats, MMstates, how='inner', on=['School'])
