import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from data.transfers.process_transfers import transfers_five_year_table
from data.league_tables.process_tables import avg_pos_3_seasons
from abrev import team_abbreviations

'''
Average finish vs money spent (2021 - 2024) 3 seasons 
'''

teams_data = {}
for entry in transfers_five_year_table:
    if entry["Team"] in avg_pos_3_seasons:
        teams_data[entry["Team"]] = (-entry["last3"], avg_pos_3_seasons[entry["Team"]])

print(teams_data)

team_names = list(teams_data.keys())
net_transfer_spending = [data[0] for data in teams_data.values()]
average_points = [data[1] for data in teams_data.values()]

# Create the scatter plot
plt.scatter(net_transfer_spending, average_points)

# Annotate each point with the team name (2 for formatting)
for team_name, data in teams_data.items():
        plt.annotate(team_abbreviations[team_name],  # this is the text
                    data,  # these are the coordinates to position the label
                    textcoords="offset points",  # how to position the text
                    xytext=(0,5),  # distance from text to points (x,y)
                    ha='center')  # horizontal alignment can be left, right or center

# Set the title and labels for the axes
plt.title('Net Transfer Spending vs Average League Position Since 2021')
plt.xlabel('Net Transfer Spending(€ in millions)')
plt.ylabel('Average Points per Season')

plt.gca().invert_yaxis()


# Show the plot
plt.show()
