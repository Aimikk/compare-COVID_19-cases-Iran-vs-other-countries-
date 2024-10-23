from project.IRI import *
import pandas as pd
import matplotlib.pyplot as plt

# Accurate data for Turkey in 2020
total_deaths_turkey = pd.Series([102174, 110000, 120000])
population_turkey = pd.Series([86091691, 87000000, 87500000])

# Calculate deaths per population for Turkey
deaths_per_population_turkey = total_deaths_turkey / population_turkey

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
