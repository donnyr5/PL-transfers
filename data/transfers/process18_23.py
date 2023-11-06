import csv

def convert_value_to_million(value):
    # Remove the '€' symbol
    value = value.replace('€', '')

    if value.endswith('m'):         #stays same
        return float(value[:-1])
    elif value.endswith('k'):       #divide 1000
        return float(value[:-1]) / 1000
    elif value.endswith('n'):
        return float(value[:-2]) * 1000
    else:
        return float(value)         #if nothing assume millions I guess

#export
transfers18_23 = []

csv_file_path = './data/transfers/18:23.csv'
with open(csv_file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile) # Create a CSV reader object

    for row in csvreader:
        # Create a dictionary for each team, going through rows
        team_data = {
            'Team': row[1],
            'Expenditure': convert_value_to_million(row[2]),
            'Arrivals': row[3],
            'Income': convert_value_to_million(row[4]),
            'Departures': row[5],
            'Balance': convert_value_to_million(row[6]),
        }
        transfers18_23.append(team_data) #add each row

# Print out the list of dictionaries
# for team in transfers_five_year_table:
#     print(team)

# print(transfers_two_year_table)
'''
value is in millions of EURO
'''
# print(transfers18_23)