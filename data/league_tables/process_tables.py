import os

# Define the base directory where your CSV files are located
base_dir = './data/league_tables/'
# Define the range of your seasons
seasons = range(12, 24)  # This will cover seasons from '12:13' to '22:23'

# team_data[season] = the entire table for that season
# team_data[season][1] = data for team that finished 2nd that season.
# team_data[season][1]["Pts"] = points for 2nd place team that year.
team_data = {}

for start_year in seasons:
    # Format the season string correctly with leading zero for years less than 10
    season = f"{start_year:02d}:{start_year+1:02d}"
    file_name = f"{season}_table.csv"
    file_path = os.path.join(base_dir, file_name)

    try:
        with open(file_path, 'r') as file:
            text = file.read()

        # Split text into lines and ignore empty lines or lines with only empty strings
        lines = [line for line in text.strip().split("\n") if line and not line.strip().isspace()]

        # Assume that the second line contains the headers
        headers = ['Position', 'Team'] + [h.strip('"') for h in lines[1].split(',')[2:] if h.strip('"')]

        # Initialize a list to hold data for the current season
        season_data = []

        for line in lines[2:]:  # Skip the header lines
            values = [v.strip('"') for v in line.split(',')]
            # Create a dictionary for each team using the headers
            data_dict = dict(zip(headers, values))
            season_data.append(data_dict)

        # Add the processed season data to the team_data dictionary
        team_data[season] = season_data

    except FileNotFoundError:
        print(f"File not found for season {season}, skipping.")
    except Exception as e:
        print(f"An error occurred while processing season {season}: {e}")

# Now, team_data is a dictionary where each key is a season and each value is the list of team data for that season
# Example usage:
# for season, data in team_data.items():
#     if data:  # Check if there is data for the season
#         print(f"Season: {season}, Team in 1st place: {data[0]['Team']}")
#     else:
#         print(f"Season: {season} has no data.")

# now we have data from every season's table. lets get average points of each team.

'''
1. store each teams avg points
2. we have to know how many seasons a team in the league.
'''
#EXPORT THESE
avg_pts_5_seasons = {}
avg_pos_3_seasons = {}


season_keys = list(team_data.keys())
recent_5_seasons = season_keys[6:11] #last 5 seasons
season_count = {}

total_points_5_seasons = {}
for season in recent_5_seasons:
    for entry in team_data[season]:
        if entry['Team'] in total_points_5_seasons:
            total_points_5_seasons[entry['Team']] += int(entry["Pts"])
            season_count[entry['Team']] += 1
        else:
            total_points_5_seasons[entry['Team']] = int(entry["Pts"])
            season_count[entry['Team']] = 1

for team in total_points_5_seasons:
    avg_pts_5_seasons[team] = round(total_points_5_seasons[team] / season_count[team], 2)

#get average finish from last 2 seasons + right now. have this for every team in the league now.
recent_2_seasons = season_keys[9:] #last 5 seasons
season_count = {}

total_points_2_seasons = {}
for season in recent_2_seasons:
    for entry in team_data[season]:
        if entry['Team'] in total_points_2_seasons:
            total_points_2_seasons[entry['Team']] += int(entry["Position"])
            season_count[entry['Team']] += 1
        else:
            total_points_2_seasons[entry['Team']] = int(entry["Position"])
            season_count[entry['Team']] = 1

for team in total_points_2_seasons:
    avg_pos_3_seasons[team] = round(total_points_2_seasons[team] / season_count[team], 2)

#each team and their average points last 5 seasons. 
# print(avg_pts_5_seasons)
# print(avg_pos_3_seasons)
# print(avg_pts_5_seasons)
