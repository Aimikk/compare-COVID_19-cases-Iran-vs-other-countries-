from project.IRI import *
import pandas as pd
import matplotlib.pyplot as plt

total_deaths_usa = pd.Series([100000, 105000, 110000])
population_usa = pd.Series([331000000, 332000000, 333000000 ])

# Calculate deaths per population for the USA
deaths_per_population_usa = total_deaths_usa / population_usa
# Print both death per population
print(deaths_per_population_usa)
print(deaths_per_population_iran)

# Plotting
plt.figure(figsize=(12, 6))

plt.plot(deaths_per_population_iran, label='Iran', marker='o', linestyle='-', color = 'r')
plt.plot(deaths_per_population_usa, label='USA', marker='s', linestyle='--' , color = 'g')

plt.annotate('First Peak', xy=(0, deaths_per_population_iran.iloc[0]), xytext=(0, deaths_per_population_iran.iloc[0]*1.1),arrowprops=dict(facecolor='black', shrink=0.05))
plt.xlabel('Index')
plt.ylabel('Deaths per Population')
plt.title('Comparison of Deaths per Population: Iran vs USA')
plt.legend()
plt.grid(True)
plt.show()
