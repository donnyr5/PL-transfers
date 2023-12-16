import pandas as pd

raw_data = pd.read_csv("./data/detailed_transfers/premier-league.csv")

def convert_value_to_million(value):
    # Remove the '€' symbol
    value = value.replace('€', '')

    if value[0].isalpha():
        return 0
    elif value.endswith('m'):         #stays same
        return float(value[:-1])
    elif value.endswith('Th.'):       #divide 1000
        value = value.replace('Th.', '')
        return float(value) / 1000
    elif value.endswith('Th'):       #divide 1000
        value = value.replace('Th.', '')
        return float(value) / 1000
    elif value.endswith('k'):       #divide 1000
        value = value.replace('k', '')
        return float(value) / 1000
    elif value.endswith('-') or value.endswith('?'):
        return 0
    else:
        return float(value)         #if nothing assume millions I guess


# clubs is list of each club which made transfers.
clubs = []
data_recent = raw_data[ (raw_data['year'] >= 2018) & (raw_data['transfer_movement'] == 'in')]
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

position_histogram_raw = position_histogram

#modify it for readability.
position_histogram["Right Winger"] += position_histogram['Right Midfield']
position_histogram["Left Winger"] += position_histogram['Left Midfield']
del position_histogram['Right Midfield']
del position_histogram['Left Midfield']
#striker
position_histogram["Centre-Forward"] += position_histogram["Second Striker"]
del position_histogram["Second Striker"]
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


'''
Avg money spent on each position
'''
position_spending = {}

#loop though the data frame
for row in data_recent.itertuples():
    if position_spending.__contains__(row.position):                                
        position_spending[row.position] += convert_value_to_million(row.fee)
    else:
        position_spending[row.position] = convert_value_to_million(row.fee)
    
    position_spending[row.position] += 1

    # print("row fee:", row.fee, "    Position: ", row.position, "    value: ", convert_value_to_million(row.fee))

position_spending["Right Winger"] += position_spending['Right Midfield']
position_spending["Left Winger"] += position_spending['Left Midfield']
del position_spending['Right Midfield']
del position_spending['Left Midfield']
#striker
position_spending["Centre-Forward"] += position_spending["Second Striker"]
del position_spending["Second Striker"]
#winger
position_spending['Winger'] = position_spending['Left Winger'] + position_spending['Right Winger']
position_spending['Full Back'] = position_spending['Right-Back'] + position_spending['Left-Back']
del position_spending['Left Winger']
del position_spending['Right Winger']
del position_spending['Left-Back']
del position_spending['Right-Back']
#midfield
position_spending["Midfielder"] = position_spending["Central Midfield"] + position_spending["Defensive Midfield"] + position_spending["Attacking Midfield"]
del position_spending['Attacking Midfield']
del position_spending['Central Midfield']
del position_spending['Defensive Midfield']

for key in position_spending:
    position_spending[key] = position_spending[key]/ position_histogram[key]
# print(position_spending)



#one summer of transfers-- how much does that spending predict a point increase?
'''
transfer spending vs point difference from 2018-2019 to 2019-2020 
'''




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