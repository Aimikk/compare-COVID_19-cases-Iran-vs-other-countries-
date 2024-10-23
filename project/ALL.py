from project.IRI import *
from project.S_korea import *
from project.SPA import *
from project.USA import *
from project.TURKEY import *

# Plotting
plt.figure(figsize=(12, 6))

plt.plot(deaths_per_population_iran, label='Iran', marker='o', linestyle='-', color = 'r')
plt.plot(deaths_per_population_spain, label='Spain', marker='s', linestyle='--' , color = 'g')
plt.plot(deaths_per_population_korea, label='South Korea', marker='^', linestyle='-.', color='b')
plt.plot(deaths_per_population_turkey, label='Turkey', marker='*', linestyle='-.', color='c')
plt.plot(deaths_per_population_usa, label='USA', marker='p', linestyle='--' , color = 'm')

plt.xlabel('Index')
plt.ylabel('Deaths per Population')
plt.title('Comparison of Deaths per Population: Iran vs All')
plt.legend()
plt.grid(True)
plt.show()
