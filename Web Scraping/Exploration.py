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