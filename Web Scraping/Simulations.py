import pandas as pd
import numpy as np
import math
from scipy.stats import norm
from numpy.random import uniform
import matplotlib.pyplot as plt

# Reading in the dataset
AllStats = pd.read_csv("AllStats.csv")
AllStats

# This is where the teams are chosen for the simulation
team1 = "Rutgers"
team2 = "Temple"

# Assigns variables to team 1
Team1PF = AllStats.loc[AllStats['Team'] == team1, 'Points For'].values[0]
Team1PA = AllStats.loc[AllStats['Team'] == team1, 'Points Against'].values[0]
Team1SDPF = AllStats.loc[AllStats['Team'] == team1, 'Standard Deviation'].values[0]

# Assigns variables to team 2
Team2PF = AllStats.loc[AllStats['Team'] == team2, 'Points For'].values[0]
Team2PA = AllStats.loc[AllStats['Team'] == team2, 'Points Against'].values[0]
Team2SDPF = AllStats.loc[AllStats['Team'] == team2, 'Standard Deviation'].values[0]

# Creates Adjusted points for both teams based on values from each team
Team1ADJ = math.sqrt(Team1PF * Team2PA)
Team2ADJ = math.sqrt(Team2PF * Team1PA)

# Generates one score for team 1
norm.ppf(
  uniform(0, 1),
  loc=Team1ADJ,
  scale=Team1SDPF
)

# Generates one score for team 2
norm.ppf(
  uniform(0, 1),
  loc=Team2ADJ,
  scale=Team2SDPF
)

# Names variables used for simulation
N = 10000
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

# Plots the relative frequencies as a bar chart
plt.bar(x=rel_freq.index, height=rel_freq.values)

# Plots Bar Graph and exact values for the Monte Carlo Simulation
plt.show()
print(table)