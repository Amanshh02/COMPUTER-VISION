import matplotlib.pyplot as plt
import numpy as np

labels = ['A', 'B', 'C']
values = [1, 4, 2]

# Resize figure **before** plotting
plt.figure(figsize=(6, 4))

# Create bar plot
bars = plt.bar(labels, values)

# Apply hatching to each bar
for bar in bars:
    bar.set_hatch('/')

plt.legend()

# Show the plot
plt.show()
