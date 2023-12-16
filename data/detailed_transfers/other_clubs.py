import pandas as pd

raw_data = pd.read_csv("./data/detailed_transfers/premier-league.csv")

'''
Most common clubs purchased from(selling_clubs) and sold to (buying_clubs)
'''
buying_clubs = {}
selling_clubs = {}

data_recent = raw_data[ (raw_data['year'] >= 2018) ]


for row in data_recent.itertuples():
    if (row.transfer_movement == 'in'):
        if selling_clubs.__contains__(row.club_involved_name):
            selling_clubs[row.club_involved_name] += 1
        else:
            selling_clubs[row.club_involved_name] = 1
    if (row.transfer_movement == 'out'):
        if buying_clubs.__contains__(row.club_involved_name):
            buying_clubs[row.club_involved_name] += 1
        else:
            buying_clubs[row.club_involved_name] = 1


buying_clubs = sorted(buying_clubs.items(), key=lambda item: item[1], reverse=True)
selling_clubs = sorted(selling_clubs.items(), key=lambda item: item[1], reverse=True)

del buying_clubs[0]

# print(buying_clubs[0:10])
where_are_players_going = buying_clubs[0:15]
where_are_players_coming_from = selling_clubs[0:15]

# for data in buy_and_sell:
