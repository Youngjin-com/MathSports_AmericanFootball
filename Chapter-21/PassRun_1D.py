###########################################################################
### Chapter 21 - Football Decision Making 101                           ###
# Mathletics: How Gamblers, Managers, and Sports Enthusiasts              #
# Use Mathematics in Baseball, Basketball, and Football                   #
###########################################################################

import pandas as pd
import numpy as np
import scipy.stats
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv("pbp_1618.csv")
#epv = pd.read_csv("CWS.csv")

print("Pass-Run Ration on 1st and 10 at our own 25")
print(dataset["play_type"].value_counts())


#epa = [(epv[(epv.Down == 2) & (epv.Ydstogo == 10-dataset['yards_gained'].iloc[i])& (epv.Line == 25+dataset['yards_gained'].iloc[i])]["Value"].reset_index()['Value'][0]-epv[(epv.Down == 1) & (epv.Ydstogo == 10) & (epv.Line == 25)]["Value"].reset_index()['Value'][0]) if dataset['yards_gained'].iloc[i] < 10 else (epv[(epv.Down == 1) & (epv.Ydstogo == min(10,100-(25 + dataset['yards_gained'].iloc[i]))) & (epv.Line == 25 + dataset['yards_gained'].iloc[i])]["Value"].reset_index()['Value'][0]-epv[(epv.Down == 1) & (epv.Ydstogo == 10) & (epv.Line == 25)]["Value"].reset_index()['Value'][0]) for i in range(len(dataset))]


pass_epa = dataset[dataset.play_type == "pass"]["epa"]
run_epa = dataset[dataset.play_type == "run"]["epa"]

#kde_pass = scipy.stats.gaussian_kde(pass_epa)
#kde_run = scipy.stats.gaussian_kde(run_epa)

#grid = np.arange(-6, 6)
matplotlib.rcParams.update({'font.size': 15})
#fig, ax = plt.subplots(2,1)
#sns.distplot(pass_epa,ax = ax[0]);
#sns.distplot(run_epa,ax = ax[1]);
#ax.plot(grid, kde_pass(grid), lw=2, label = "Pass")
#ax.plot(grid, kde_run(grid), lw=2, label = "Run")
#plt.xlabel("Expected Points Added (Pass)")
#plt.ylabel("Probability Density")
#plt.savefig("Pass-EPA.png")

fig = plt.figure()
ax1 = fig.add_axes(ylim=(-8,8))
ax2 = fig.add_axes(ylim=(-8,8))
sns.distplot(pass_epa,ax = ax1,label="Pass")
sns.distplot(run_epa,ax = ax2,label="Run")
plt.xlabel("Expected Points Added")
plt.ylabel("Probability Density")
plt.legend()
plt.savefig("Pass-Run-EPA.png")

