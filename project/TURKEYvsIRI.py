from project.IRI import *
from project.TURKEY import *
import pandas as pd
import matplotlib.pyplot as plt

# Print deaths per population
print(deaths_per_population_iran)
print(deaths_per_population_turkey)

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(deaths_per_population_iran, label='Iran', marker='o', linestyle='-', color='r')
plt.plot(deaths_per_population_turkey, label='Turkey', marker='^', linestyle='-.', color='b')

# Add annotations
plt.annotate('First Peak', xy=(0, deaths_per_population_iran.iloc[0]), xytext=(0, deaths_per_population_iran.iloc[0]*1.1),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.xlabel('Index')
plt.ylabel('Deaths per Population')
plt.title('Comparison of Deaths per Population: Iran vs Turkey')
plt.legend()
plt.grid(True)
plt.show()
