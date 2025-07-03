import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# #  basic graph
# plt.plot([1,2,3],[2,4,6])
# plt.show()

x=[2,4,6]
y=[3,5,7]

#resize
plt.figure(figsize=(5,3), dpi=300)

#label,color,linewidth
# plt.plot(x,y, label='2x', color='black', linewidth=2, marker='.',markersize='10', linestyle='--',markeredgecolor='blue')

#short-hand notation = color-marker-line notation
plt.plot(x, y, 'r.--',label='2x', )


# Font dictionary
plt.title("Our first graph", fontdict={'fontname': 'Comic Sans MS'})
plt.xlabel('X-Axis', fontdict={'fontname' : 'algerian'})
plt.ylabel('Y-Axis', fontdict={'fontname' : 'algerian'})

#ticks : plot on the ticks 
plt.xticks([0,3,5,7])
plt.yticks([0,2,4,6])

# Legend
plt.legend()

plt.show()

## Line-2
x2 = np.arange(0,4,0.5) ## start,end,tick
plt.plot(x2, x2**2,'r')
plt.title('x^2')
plt.show()

