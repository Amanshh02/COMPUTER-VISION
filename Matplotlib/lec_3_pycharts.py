import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

fifa = pd.read_csv("Matplotlib/fifa_data.csv")
print(fifa.head(5))

left = fifa.loc[fifa['Preferred Foot'] == 'Left'].count()[0]
right = fifa.loc[fifa['Preferred Foot'] == 'Right'].count()[0]
print(left)
print(right)

colors = ['#abcdef', 'pink']

label = ['left', 'right']
plt.pie([left, right], labels= label, colors = colors, autopct='%.2f')

plt.title('Foot preferrence')

# plt.show()

# New Topic

print(fifa.Weight.head(5))

fifa.Weight = [x.strip('lbs') for x in fifa.weight]

print(fifa.Weight.head(5))