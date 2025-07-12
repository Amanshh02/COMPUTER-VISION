import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

gas = pd.read_csv('Matplotlib/gas_prices.csv')
print(gas)

#line graphs

plt.figure(figsize=(10,10))

plt.title('Gas Prices over time (USD)', fontdict={'fontweight' : 'bold', 'fontsize' : 18})

# To put country one by one

# plt.plot(gas.Year, gas.USA,'b.-' , label='United states')
# plt.plot(gas.Year, gas.Canada, 'r.-', label='Canada')
# plt.plot(gas.Year, gas['South Korea'], 'g.-', label='South Korea')

# To put country using for loop

for country in gas:
    if country != "Year":
        plt.plot(gas.Year, gas[country], marker='.',label=country)

plt.xlabel("Year")
plt.ylabel("USD")

plt.xticks(gas.Year[::3])

plt.legend()

plt.savefig("Gas_Prices.png", dpi=300)


plt.show()
