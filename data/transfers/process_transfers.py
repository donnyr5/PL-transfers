import csv

def convert_value_to_million(value):
    # Remove the '€' symbol
    value = value.replace('€', '')

    if value.endswith('m'):         #stays same
        return float(value[:-1])
    elif value.endswith('k'):       #divide 1000
        return float(value[:-1]) / 1000
    else:
        return float(value)         #if nothing assume millions I guess


# EXPORT THIS
transfers_five_year_table = []

csv_file_path = './data/transfers/5_year_totals.csv'
with open(csv_file_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile) # Create a CSV reader object
    headers = next(csvreader)
    

    for row in csvreader:
        # Create a dictionary for each team, going through rows
        team_data = {
            'Team': row[0],
            '23/24': convert_value_to_million(row[1]),
            '22/23': convert_value_to_million(row[2]),
            '21/22': convert_value_to_million(row[3]),
            '20/21': convert_value_to_million(row[4]),
            '19/20': convert_value_to_million(row[5]),
            'Total': convert_value_to_million(row[6]),
        }
        transfers_five_year_table.append(team_data) #add each row

# Print out the list of dictionaries
# for team in transfers_five_year_table:
#     print(team)

'''
value is in millions of EURO
'''