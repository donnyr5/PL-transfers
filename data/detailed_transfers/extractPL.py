import pandas as pd


raw_data = pd.read_csv("./data/detailed_transfers/premier-league.csv")

# clubs is list of each club which made transfers.
clubs = []
data_recent = raw_data[ raw_data['year'] >= 2018 ]
clubs_raw = data_recent['club_name']
for team in clubs_raw:
    if (clubs.count(team) == 0):
        clubs.append(team)




'''
Average age of transfers per club from 2018-2022 (use up to 22/23 table)
'''
avg_age = {}

for team in clubs:
    club_data = raw_data[(raw_data['club_name'] == team) & (raw_data['transfer_movement'] == 'in')]
    # print(club_data)

    # get average age
    total_age = 0
    for age in club_data['age']:
        total_age += age
    
    if total_age > 0:
        avg_age[team] = total_age/len(club_data)
    else:
        avg_age[team] = 0


'''
Most commonly transfered in position.
'''
position_data = data_recent['position']
position_histogram = {}
for data in position_data:
    if (position_histogram.__contains__(data)):
        position_histogram[data] += 1
    else:
        position_histogram[data] = 1

#modify it for readability.
'''
Categories:
Winger
Centre-Forward
Midfielder
Full Back
CB
Goalkeeper
'''

position_histogram["Right Winger"] += position_histogram['Right Midfield']
position_histogram["Left Winger"] += position_histogram['Left Midfield']
del position_histogram['Right Midfield']
del position_histogram['Left Midfield']

#striker
position_histogram["Centre-Forward"] += position_histogram["Second Striker"]
del position_histogram["Second Striker"]
del position_histogram['attack']

#winger
position_histogram['Winger'] = position_histogram['Left Winger'] + position_histogram['Right Winger']
position_histogram['Full Back'] = position_histogram['Right-Back'] + position_histogram['Left-Back']
del position_histogram['Left Winger']
del position_histogram['Right Winger']
del position_histogram['Left-Back']
del position_histogram['Right-Back']

#midfield
position_histogram["Midfielder"] = position_histogram["Central Midfield"] + position_histogram["Defensive Midfield"] + position_histogram["Attacking Midfield"]
del position_histogram['Attacking Midfield']
del position_histogram['Central Midfield']
del position_histogram['Defensive Midfield']



# print(position_histogram)


def remove_FCs(list):
    list['Liverpool'] = list['Liverpool FC']
    del list['Liverpool FC']

    list['Chelsea'] = list['Chelsea FC']
    del list['Chelsea FC']

    list['Arsenal'] = list['Arsenal FC']
    del list['Arsenal FC']

    list['Everton'] = list['Everton FC']
    del list['Everton FC']

    list['Watford'] = list['Watford FC']
    del list['Watford FC']

    list['Burnley'] = list['Burnley FC']
    del list['Burnley FC']

    list['Southampton'] = list['Southampton FC']
    del list['Southampton FC']

    list['Fulham'] = list['Fulham FC']
    del list['Fulham FC']

    list['Brentford'] = list['Brentford FC']
    del list['Brentford FC']

    return


remove_FCs(avg_age)
# print(avg_age)