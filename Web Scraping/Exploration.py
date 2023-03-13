import pandas as pd

fullstats = pd.read_csv("fullstats.csv")

import matplotlib.pyplot as plt

# Create scatter plot
plt.scatter(fullstats.Seed, fullstats["SOS AdjEM"])

# Add axis labels and title
plt.xlabel('X-axis label')
plt.ylabel('Y-axis label')
plt.title('Scatter plot')

# Display the plot
plt.show()


# This plot is interesting because it very clearly shows the disparity of schedules between seeds 1-11 and 12-16. 
# The reason that is interesting is because seeds 12-16 are usually the teams that auto-qualify from the 1-bid conferences
# showing that if you do not play a high level of competition it is very unlikely that you can make the tournament

# Create scatter plot
plt.scatter(fullstats.AdjT, fullstats.PPG)

# Add axis labels and title
plt.xlabel('Adjusted Tempo')
plt.ylabel('Points Scored Per Game')
plt.title('Scatter plot')

# Display the plot
plt.show()

# This graph confirms that the faster the team plays the more points they will score. Nonetheless there are outliers that
# fall outside the congregation in the middle of the graph.

# Create scatter plot
plt.scatter(fullstats.AdjT, fullstats.OppPPG)

# Add axis labels and title
plt.xlabel('Adjusted Tempo')
plt.ylabel('Points Allowed Per Game')
plt.title('Scatter plot')

# Display the plot
plt.show()

# Similar to the previous figure, this chart shows the upward trend between points allowed and tempo. However the center 
# looks to be more condensed as it's likely the teams tempo has more of an impact on themselves as opposed to their opponent

# Create scatter plot
plt.scatter(fullstats["AdjEM Rank"], fullstats.Wins, c = fullstats.Seed)

# Add axis labels and title
plt.xlabel('Strength of Schedule Rank')
plt.ylabel('Wins')
plt.title('Scatter plot')
plt.colorbar()

# Display the plot
plt.show()

# While it may have been obvious already, this chart shows that teams must have a good combination between wins and strength
# of schedule to earn a high seed, if you do not play other good teams it is unlikely you earn a top seed.

import plotly.express as px

# Group by state and count the occurrences of each two-letter abbreviation
state_counts = fullstats['State'].value_counts().reset_index(name='count').rename(columns={'index': 'state'})

# Create a choropleth map
fig = px.choropleth(state_counts, locations='state', locationmode='USA-states', color='count',
                    scope='usa', color_continuous_scale='YlOrRd')

# Set title and colorbar label
fig.update_layout(title_text='Count of Two-Letter Abbreviations by State')
fig.update_coloraxes(colorbar_title='Count')

# Show the plot
fig.show()

# The field seems to be made up of mainly teams from Texas, California, Virginia, New York, North Carolia and Ohio. The two
# states that stand the most are Texas and North Carolina as Texas features a lot of Power 5 schools, while North Carolina 
# is top heavy having perennial favorites such as North Carolina and Duke that make the field almost every year.
# Create scatter plot
plt.scatter(fullstats['AdjO Rank'], fullstats['AdjD Rank'], c = fullstats.Seed)

# Add axis labels and title
plt.xlabel('Adjusted Offensive Efficiency')
plt.ylabel('Adjusted Defensive Efficiency')
plt.title('Seed by Adjusted Efficiencies')
plt.colorbar()

# Display the plot
plt.show()

# This graph is interesting as it shows the difference in rankings between the seeds, most teams that wind up 6th or higher 
# are Top 50 in offensive and defensive efficiences while the 15 and 16 seeds are very separated from the rest of the pack.

# Create scatter plot
plt.scatter(fullstats['Overall Seed'], fullstats['Luck'])

# Add axis labels and title
plt.xlabel('Overall Seed')
plt.ylabel('')
plt.title('Seed by Adjusted Efficiencies')

# Display the plot
plt.show()

# This scatterplot shows that luck is not a big factor when it comes to team seeding as it is relatively evenly distributed

avg_seed_by_conf = fullstats.groupby('Berth type')['AdjEM Rank'].mean()

# create bar chart
plt.barh(avg_seed_by_conf.index, avg_seed_by_conf.values)

# Adds axis labels and title
plt.xlabel('Conference')
plt.ylabel('Average Seed')
plt.title('Average Seed by Conference')
plt.show()

# A simple bar chart that shows that teams who make it in without winning their conference usually play a harder schedule
# This is likely due to the one-bid conferences playing easier schedules, and never sending more than 1 team

# Filters the dataframe to only include at-large bids
at_large = fullstats[fullstats['Berth type'] == 'At-Large']

# Calculates the average seed for each conference's at-large bids
conf_avg_seed = at_large.groupby('Conference')['Seed'].mean()

# Sorts the resulting dataframe by the average seed in ascending order
conf_avg_seed = conf_avg_seed.sort_values()

# Creates a horizontal bar chart
plt.figure(figsize=(10,6)) 
conf_avg_seed.plot.barh()
plt.title('Average Seed of At-Large Bids by Conference')
plt.xlabel('Seed') 
plt.ylabel('Conference') 
plt.show()

# An interesting chart that shows average at-large seed for each conference. Some conferences have not had at large teams
# in the past 10 years, so they have been left out. The Big East, ACC, Big 12, Big Ten and SEC have a lead over the rest of
# the conferences. The MAAC only had one 14 seed, which is interesting that an at-large team was seeded 14th as that it rare