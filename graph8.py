import numpy as np
import matplotlib.pyplot as plt
from abrev import team_abbreviations
from data.transfers.process18_23 import transfers18_23

'''
Spending last 5 years (Figure 1)
'''
#removing non-current PL teams
transfers18_23 = transfers18_23[0:24]
del transfers18_23[23]
del transfers18_23[20]
del transfers18_23[13]
del transfers18_23[11]



teams = []
spendings = []
balance = []

for entry in transfers18_23:
    teams.append(team_abbreviations[entry["Team"]])
    balance.append(entry["Balance"])
    spendings.append(-entry["Expenditure"])

X_axis = np.arange(len(teams))

plt.bar(X_axis - 0.2, spendings, 0.4, label = 'Spending') 
plt.bar(X_axis + 0.2, balance, 0.4, label = 'Net Losses') 
plt.xticks(X_axis, teams)

plt.title("Transfer Spending over 2018/19 - 2022/23 Seasons")
plt.xlabel("Club")
plt.ylabel("5-year Total (million Euros)")
plt.gca().invert_yaxis()
plt.legend()
plt.show()

'''
X = ['Group A','Group B','Group C','Group D'] 
Ygirls = [10,20,20,40] 
Zboys = [20,30,25,30] 
  
X_axis = np.arange(len(X)) 
  
plt.bar(X_axis - 0.2, Ygirls, 0.4, label = 'Girls') 
plt.bar(X_axis + 0.2, Zboys, 0.4, label = 'Boys') 
  
plt.xticks(X_axis, X) 
plt.xlabel("Groups") 
plt.ylabel("Number of Students") 
plt.title("Number of Students in each group") 
plt.legend() 
plt.show() 
'''