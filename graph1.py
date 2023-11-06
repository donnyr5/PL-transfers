import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from data.league_tables.process_tables import avg_pts_5_seasons
from data.transfers.process18_23 import transfers18_23
from data.transfers.process_transfers import transfers_five_year_table

'''
Average points per season VS net transfer spending (in million euro) from 2018/19 - 2022/2023
'''
team_abbreviations = {
    "Manchester City": "MCI",
    "Arsenal": "ARS",
    "Manchester United": "MUN",
    "Newcastle United": "NEW",
    "Liverpool": "LIV",
    "Brighton & Hove Albion": "BHA",
    "Aston Villa": "AVL",
    "Tottenham Hotspur": "TOT",
    "Brentford": "BRE",
    "Fulham": "FUL",
    "Crystal Palace": "CP",
    "Chelsea": "CHE",
    "Wolverhampton Wanderers": "WOL",
    "West Ham United": "WHU",
    "AFC Bournemouth": "BOU",
    "Nottingham Forest": "NFO",
    "Everton": "EVE",
    "Leicester City": "LEI",
    "Leeds United": "LEE",
    "Southampton": "SOU",
    'Sheffield United': "SHU",
    "Burnley": "BUR",
    "Luton Town": "LUT",
    "Norwich City": "NOR",
    "West Bromwich Albion": "WBA",
    "Cardiff City": "CAR",
    "Huddersfield Town": "HUD"
}

# point for each team(money spent, pts)
teams_data = {}
for entry in transfers18_23:
    if entry["Team"] in avg_pts_5_seasons:
        teams_data[entry["Team"]] = (-entry["Balance"], avg_pts_5_seasons[entry["Team"]])

# print(transfers_five_year_table)

# print(teams_data)

# Extract the team names, net transfer spending, and average points into separate lists
team_names = list(teams_data.keys())
net_transfer_spending = [data[0] for data in teams_data.values()]
average_points = [data[1] for data in teams_data.values()]

# Create the scatter plot
plt.scatter(net_transfer_spending, average_points)

# Annotate each point with the team name (2 for formatting)
for team_name, data in teams_data.items():
    if team_abbreviations[team_name] == "NEW" or team_abbreviations[team_name] == "AVL":
        plt.annotate(team_abbreviations[team_name],  # this is the text
                    data,  # these are the coordinates to position the label
                    textcoords="offset points",  # how to position the text
                    xytext=(-16,-5),  # distance from text to points (x,y)
                    ha='center')  # horizontal alignment can be left, right or center
    else:
        plt.annotate(team_abbreviations[team_name],  # this is the text
                    data,  # these are the coordinates to position the label
                    textcoords="offset points",  # how to position the text
                    xytext=(0,5),  # distance from text to points (x,y)
                    ha='center')  # horizontal alignment can be left, right or center

# Set the title and labels for the axes
plt.title('Net Transfer Spending vs Average Points per Season (18-23)')
plt.xlabel('Net Transfer Spending Last 5 Seasons (€ in millions)')
plt.ylabel('Average Points Per Season')

# Show the plot
plt.show()