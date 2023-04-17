import pandas as pd
import numpy as np
import math
from scipy.stats import norm
from numpy.random import uniform
import matplotlib.pyplot as plt

print("1 Purdue")
print("——————————————| 1 Purdue")
print("16 FDU        |——————————————|")
print("——————————————|              | 9 FAU")
print("8 Memphis                    |——————————————")
print("——————————————| 9 FAU        |")
print("9 FAU         |——————————————|")
print("——————————————|")

AllStats = pd.read_csv("AllStats.csv")
AllStats

def Simulate(team1, team2, N):
    # Assigns variables to team 1
    Team1PF = AllStats.loc[AllStats['Team'] == team1, 'Points For'].values[0]
    Team1PA = AllStats.loc[AllStats['Team'] == team1, 'Points Against'].values[0]
    Team1SDPF = AllStats.loc[AllStats['Team'] == team1, 'Standard Deviation'].values[0]

    # Assigns variables to team 2
    Team2PF = AllStats.loc[AllStats['Team'] == team2, 'Points For'].values[0]
    Team2PA = AllStats.loc[AllStats['Team'] == team2, 'Points Against'].values[0]
    Team2SDPF = AllStats.loc[AllStats['Team'] == team2, 'Standard Deviation'].values[0]

    Team1ADJ = math.sqrt(Team1PF * Team2PA)
    Team2ADJ = math.sqrt(Team2PF * Team1PA)

    # Names variables used for simulation
    outcome = np.empty(N, dtype='object')

    # Runs the simulation 10,000 times
    for i in range(N):
        d = (np.random.normal(loc=Team1ADJ, scale=Team1SDPF) -
             np.random.normal(loc=Team2ADJ, scale=Team2SDPF))
        d = team1 if d > 0 else team2
        outcome[i] = d
    
    # Makes variables to help with visualization
    outcome_series = pd.Series(outcome)
    table = outcome_series.value_counts()
    rel_freq = table / table.sum()
    return(table)
    

teams = ["Alabama", "Texas A&M-CC", "Maryland", "West Virginia", "San Diego St", "Charleston", "Virginia", "Furman", "Creighton", "NC State", "Baylor", "UCSB", "Missouri", "Utah St.", "Arizona", "Princeton", "Purdue", "FDU", "Memphis", "FAU", "Duke", "Oral Roberts", "Tennessee", "Louisiana", "Kentucky", "Providence", "Kansas St.", "Montana St.", "Michigan St.", "USC", "Marquette", "Vermont", "Houston", "N. Kentucky", "Iowa", "Auburn", "Miami", "Drake", "Indiana", "Kent St.", "Iowa St.", "Pittsburgh", "Xavier", "Kennesaw St.", "Texas A&M", "Penn St.", "Texas", "Colgate", "Kansas", "Howard", "Arkansas", "Illinois", "Saint Mary's", "VCU", "UConn", "Iona", "TCU", "Arizona St.", "Gonzaga", "Grand Canyon", "Northwestern", "Boise St.", "UCLA", "UNC-Ash."]
i = 0
x=' '
round2teams=[]
while i < 64:
    table = Simulate(teams[i], teams[i+1], 3)
    rows = len(table)
    table = str(table)
    table = table.replace("dtype: int64", "")
    table = table.replace("  ", "")
    table = table.strip()
    table = ''.join([i for i in table if not i.isdigit()])
    if rows > 1:
        table = table[:table.index("\n")]
        table = table.strip()
    y = 14 - len(table)
    z = y * x
    table = table + z
    round2teams.append(table)
    
    i = i + 2

k = 0
round3teams = []
temp = []
while k < 32:
    temp.append(round2teams[k].strip())
    temp.append(round2teams[k + 1].strip())
    table = Simulate(temp[k], temp[k+1], 1)
    rows = len(table)
    table = str(table)
    table = table.replace("dtype: int64", "")
    table = table.replace("  ", "")
    table = table.strip()
    table = ''.join([k for k in table if not k.isdigit()])
    if rows > 1:
        table = table[:table.index("\n")]
        table = table.strip()
    y = 14 - len(table)
    z = y * x
    table = table + z
    round3teams.append(table)
    k = k + 2
    
l = 0
round4teams = []
temp2 = []
while l < 16:
    temp2.append(round3teams[l].strip())
    temp2.append(round3teams[l + 1].strip())
    table = Simulate(temp2[l], temp2[l+1], 1)
    rows = len(table)
    table = str(table)
    table = table.replace("dtype: int64", "")
    table = table.replace("  ", "")
    table = table.strip()
    table = ''.join([l for l in table if not l.isdigit()])
    if rows > 1:
        table = table[:table.index("\n")]
        table = table.strip()
    y = 14 - len(table)
    z = y * x
    table = table + z
    round4teams.append(table)
    l = l + 2

m = 0
round5teams = []
temp3 = []
while m < 8:
    temp3.append(round4teams[m].strip())
    temp3.append(round4teams[m + 1].strip())
    table = Simulate(temp3[m], temp3[m+1], 1)
    rows = len(table)
    table = str(table)
    table = table.replace("dtype: int64", "")
    table = table.replace("  ", "")
    table = table.strip()
    table = ''.join([m for m in table if not m.isdigit()])
    if rows > 1:
        table = table[:table.index("\n")]
        table = table.strip()
    y = 14 - len(table)
    z = y * x
    table = table + z
    round5teams.append(table)
    m = m + 2

n = 0
round6teams = []
temp4 = []
while n < 4:
    temp4.append(round5teams[n].strip())
    temp4.append(round5teams[n + 1].strip())
    table = Simulate(temp4[n], temp4[n+1], 1)
    rows = len(table)
    table = str(table)
    table = table.replace("dtype: int64", "")
    table = table.replace("  ", "")
    table = table.strip()
    table = ''.join([n for n in table if not n.isdigit()])
    if rows > 1:
        table = table[:table.index("\n")]
        table = table.strip()
    y = 14 - len(table)
    z = y * x
    table = table + z
    round6teams.append(table)
    n = n + 2

j = 0
while j < 64: 
    y = 14 - len(teams[j])
    z = y * x
    teams[j] = teams[j] + z
    j = j + 1
print(teams[0])
print("——————————————|" + round2teams[0])
print(teams[1] + "|——————————————|")
print("——————————————|              |" + round3teams[0])
print(teams[2] + "               |——————————————|")
print("——————————————|" + round2teams[1] +"|              |")
print(teams[3] + "|——————————————|              |")
print("——————————————|                             |" + round4teams[0])
print(teams[4] + "                              |——————————————|")
print("——————————————|" + round2teams[2] + "               |              |")
print(teams[5] + "|——————————————|              |              |")
print("——————————————|              |" + round3teams[1] + "|              |")
print(teams[6] + "               |——————————————|              |")
print("——————————————|" + round2teams[3] +"|                             |")
print(teams[7] + "|——————————————|                             |")
print("——————————————|                                            |" + round5teams[0])
print(teams[8] + "                                             |——————————————|")
print("——————————————|" + round2teams[4] + "                              |              |")
print(teams[9] + "|——————————————|                             |              |")
print("——————————————|              |" + round3teams[2] + "               |              |")
print(teams[10] + "               |——————————————|              |              |")
print("——————————————|" + round2teams[5] +"|              |              |              |")
print(teams[11] + "|——————————————|              |              |              |")
print("——————————————|                             |" + round4teams[1] + "|              |")
print(teams[12] + "                              |——————————————|              |")
print("——————————————|" + round2teams[6] + "               |                             |")
print(teams[13] + "|——————————————|              |                             |")
print("——————————————|              |" + round3teams[3] + "|                             |")
print(teams[14] + "               |——————————————|                             |")
print("——————————————|" + round2teams[7] +"|                                            |")
print(teams[15] + "|——————————————|                                            |")
print("——————————————|                                                           |" + round6teams[0])
print(teams[16] + "                                                            |——————————————|")
print("——————————————|" + round2teams[8] + "                                             |              |")
print(teams[17] + "|——————————————|                                            |              |")
print("——————————————|              |" + round3teams[4] + "                              |              |")
print(teams[18] + "               |——————————————|                             |              |")
print("——————————————|" + round2teams[9] +"|              |                             |              |")
print(teams[19] + "|——————————————|              |                             |              |")
print("——————————————|                             |" + round4teams[2] + "               |              |")
print(teams[20] + "                              |——————————————|              |              |")
print("——————————————|" + round2teams[10] + "               |              |              |              |")
print(teams[21] + "|——————————————|              |              |              |              |")
print("——————————————|              |" + round3teams[5] + "|              |              |              |")
print(teams[22] + "               |——————————————|              |              |              |")
print("——————————————|" + round2teams[11] +"|                             |              |              |")
print(teams[23] + "|——————————————|                             |              |              |")
print("——————————————|                                            |" + round5teams[1] + "|              |")
print(teams[24] + "                                             |——————————————|              |")
print("——————————————|" + round2teams[12] + "                              |                             |")
print(teams[25] + "|——————————————|                             |                             |")
print("——————————————|              |" + round3teams[6] + "               |                             |")
print(teams[26] + "               |——————————————|              |                             |")
print("——————————————|" + round2teams[13] +"|              |              |                             |")
print(teams[27] + "|——————————————|              |              |                             |")
print("——————————————|                             |" + round4teams[3] + "|                             |")
print(teams[28] + "                              |——————————————|                             |")
print("——————————————|" + round2teams[14] + "               |")
print(teams[29] + "|——————————————|              |")
print("——————————————|              |" + round3teams[7] + "|")
print(teams[30] + "               |——————————————|")
print("——————————————|" + round2teams[15] +"|")
print(teams[31] + "|——————————————|")
print("——————————————|")
print(teams[32])
print("——————————————|" + round2teams[16])
print(teams[33] + "|——————————————|")
print("——————————————|              |" + round3teams[8])
print(teams[34] + "               |——————————————|")
print("——————————————|" + round2teams[17] +"|              |")
print(teams[35] + "|——————————————|              |")
print("——————————————|                             |" + round4teams[4])
print(teams[36] + "                              |——————————————|                             |")
print("——————————————|" + round2teams[18] + "               |              |                             |")
print(teams[37] + "|——————————————|              |              |                             |")
print("——————————————|              |" + round3teams[9] + "|              |                             |")
print(teams[38] + "               |——————————————|              |                             |")
print("——————————————|" + round2teams[19] +"|                             |                             |")
print(teams[39] + "|——————————————|                             |                             |")
print("——————————————|                                            |" + round5teams[2] + "               |")
print(teams[40] + "                                             |——————————————|              |")
print("——————————————|" + round2teams[20] + "                              |              |              |")
print(teams[41] + "|——————————————|                             |              |              |")
print("——————————————|              |" + round3teams[10] + "               |              |              |")
print(teams[42] + "               |——————————————|              |              |              |")
print("——————————————|" + round2teams[21] +"|              |              |              |              |")
print(teams[43] + "|——————————————|              |              |              |              |")
print("——————————————|                             |" + round4teams[5] + "|              |              |")
print(teams[44] + "                              |——————————————|              |              |")
print("——————————————|" + round2teams[22] + "               |                             |              |")
print(teams[45] + "|——————————————|              |                             |              |")
print("——————————————|              |" + round3teams[11] + "|                             |              |")
print(teams[46] + "               |——————————————|                             |              |")
print("——————————————|" + round2teams[23] +"|                                            |              |")
print(teams[47] + "|——————————————|                                            |              |")
print("——————————————|                                                           |" + round6teams[1]+ "|")
print(teams[48] + "                                                            |——————————————|")
print("——————————————|" + round2teams[24] + "                                             |")
print(teams[49] + "|——————————————|                                            |")
print("——————————————|              |" + round3teams[12] + "                              |")
print(teams[50] + "               |——————————————|                             |")
print("——————————————|" + round2teams[25] +"|              |                             |")
print(teams[51] + "|——————————————|              |                             |")
print("——————————————|                             |" + round4teams[6] + "               |")
print(teams[52] + "                              |——————————————|              |")
print("——————————————|" + round2teams[26] + "               |              |              |")
print(teams[53] + "|——————————————|              |              |              |")
print("——————————————|              |" + round3teams[13] + "|              |              |")
print(teams[54] + "               |——————————————|              |              |")
print("——————————————|" + round2teams[27] +"|                             |              |")
print(teams[55] + "|——————————————|                             |              |")
print("——————————————|                                            |" + round5teams[3] + "|")
print(teams[56] + "                                             |——————————————|")
print("——————————————|" + round2teams[28] + "                              |")
print(teams[57] + "|——————————————|                             |")
print("——————————————|              |" + round3teams[14] + "               |")
print(teams[58] + "               |——————————————|              |")
print("——————————————|" + round2teams[29] +"|              |              |")
print(teams[59] + "|——————————————|              |              |")
print("——————————————|                             |" + round4teams[7] + "|")
print(teams[60] + "                              |——————————————|")
print("——————————————|" + round2teams[30] + "               |")
print(teams[61] + "|——————————————|              |")
print("——————————————|              |" + round3teams[15] + "|")
print(teams[62] + "               |——————————————|")
print("——————————————|" + round2teams[31] +"|")
print(teams[63] + "|——————————————|")
print("——————————————|")



