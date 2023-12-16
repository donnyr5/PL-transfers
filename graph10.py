import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from abrev import team_abbreviations
from data.league_tables.process_tables import gd_diff
from data.transfers.process_transfers import transfers_five_year_table

# from scipy import stats

'''
Change in Goal Difference vs. Net Transfer balance, Year to Year (2018-2023)
'''


#spending of each team, with all years indexed by the year.

#loop through 5 year table, and use each years transfer value in evaluating 
#x points will be transfer spending.
# y points will be point difference between years.
# (spending, point difference) for any given year.

# NOTE this only includes current premier league teams
# NOTE teams which have been in the league in non-consecutive seasons use the transfer spending of the first season. If the time period
# was longer, this would need to be adjusted, but since its relatively short, this still makes sense.

#OR I will just factor teams which have been in the league all 5 years. 


x_points = []
y_points = []

for entry in transfers_five_year_table:
    cur_team = entry["Team"]

    if gd_diff.__contains__(cur_team):
        for diff in gd_diff[cur_team]:
            y_points.append(diff[0]) #goal difference in season diff[1]

            #index by the season of transfer spending we need.
            x_points.append(-entry[diff[1]])
            # print(x,y)

plt.scatter(x_points,y_points)

plt.title("Change in Goal Difference Next Season vs. Net Transfer Balance 2018-23")
plt.xlabel("Net Transfer Balance(€ in millions)")
plt.ylabel("Change in Goal Difference, Two Consecutive Seasons")

# Calculate coefficients for the line of best fit
b, a = np.polyfit(x_points, y_points, deg=1)
# Create a polynomial function from the coefficients
line_of_best_fit = np.poly1d((b, a))
print("For 100 million a club spends, next season's goal difference is predicted to decrease by ", 100*b, ".")
# Generate y-values for each x-value using the line of best fit
plt.plot(x_points, line_of_best_fit(x_points), color='green')

plt.show()


