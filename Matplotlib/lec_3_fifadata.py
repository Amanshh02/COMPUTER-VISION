import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Loading data
fifa = pd.read_csv('Matplotlib/fifa_data.csv')
print(fifa.head(5))

# Histogram 
bins = [40,50,60,70,80,90,100]

plt.hist(fifa.Overall, bins= bins, color='abcdef')
plt.xticks(bins)


plt.ylabel('Number of players')
plt.xlabel("Skill level")
plt.xlabel('Distribution of player skills in fifa')


plt.show()