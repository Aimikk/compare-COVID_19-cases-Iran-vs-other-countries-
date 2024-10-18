import pandas as pd
import matplotlib.pyplot as plt
from project.IRI import *
from project.SPA import *

print(deaths_per_population_spain)
print(deaths_per_population_iran)
# Plotting
plt.figure(figsize=(12, 6))

plt.plot(deaths_per_population_iran, label='Iran', marker='o', linestyle='-', color = 'r')
plt.plot(deaths_per_population_spain, label='Spain', marker='s', linestyle='--' , color = 'g')

plt.annotate('First Peak', xy=(0, deaths_per_population_iran.iloc[0]), xytext=(0, deaths_per_population_iran.iloc[0]*1.1),arrowprops=dict(facecolor='black', shrink=0.05))
plt.xlabel('Index')
plt.ylabel('Deaths per Population')
plt.title('Comparison of Deaths per Population: Iran vs Spain')
plt.legend()
plt.grid(True)
plt.show()
