from project.IRI import *
import pandas as pd
import matplotlib.pyplot as plt

total_deaths_korea = pd.Series([35934, 36000, 36500])
population_korea = pd.Series([51717590, 51858482, 51800000])

# Calculate deaths per population for South Korea
deaths_per_population_korea = total_deaths_korea / population_korea

# Print deaths per population
print(deaths_per_population_iran)
print(deaths_per_population_korea)

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(deaths_per_population_iran, label='Iran', marker='o', linestyle='-', color='r')
plt.plot(deaths_per_population_korea, label='South Korea', marker='^', linestyle='-.', color='b')

# Add annotations
plt.annotate('First Peak', xy=(0, deaths_per_population_iran.iloc[0]), xytext=(0, deaths_per_population_iran.iloc[0]*1.1),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.xlabel('Index')
plt.ylabel('Deaths per Population')
plt.title('Comparison of Deaths per Population: Iran vs South Korea')
plt.legend()
plt.grid(True)
plt.show()
