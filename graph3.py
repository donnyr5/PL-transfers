import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from abrev import team_abbreviations
from data.detailed_transfers.extractPL import avg_age
from data.league_tables.process_tables import avg_pts_5_seasons

'''
Average points per season vs. average age of transfer in 18-23.
'''
# (average age, points total) for each team.
ages_points = {}
for team in avg_pts_5_seasons:
    if (avg_age[team] is not None):
        ages_points[team] = (avg_age[team], avg_pts_5_seasons[team] )

x_points = []
for data in ages_points.values():
     x_points.append(data[0])
y_points = []
for data in ages_points.values():
     y_points.append(data[1])

plt.scatter(x_points,y_points)

for team_name, data in ages_points.items():
        if (team_name == "Liverpool") or (team_name == "Manchester City") or (team_name == "Cardiff City") or (team_name == "West Bromwich Albion") or (team_name == "Arsenal") or (team_name == "Huddersfield Town") or (team_name == "Norwich City") or (team_name == "Leicester City"):
            plt.annotate(team_abbreviations[team_name],  # this is the text
                    data,  # these are the coordinates to position the label
                    textcoords="offset points",  # how to position the text
                    xytext=(0,5),  # distance from text to points (x,y)
                    ha='center')  # horizontal alignment can be left, right or center

# Set the title and labels for the axes
plt.title('Average Points per Season vs. Average age of Transfer in 2017/18 - 2022/23')
plt.xlabel('Average Age of transfer in')
plt.ylabel('Average Points per Season')

plt.show()
