import pandas as pd
import matplotlib.pyplot as plt
# Load the data from the Excel file and only read specific lines
file_path = r'C:\Users\kimia\OneDrive\Documents/DATA.xlsx'

data = pd.read_excel(file_path)
print(data)

plt.figure(figsize=(20, 10))
plt.bar(data.iloc[:, 3], data.iloc[:, 8])
plt.xlabel('year')
plt.ylabel('total cases')
plt.title('Plot of Total cases per Year')
plt.grid(True)
plt.show()



total_deaths = pd.Series([54429, 55000, 56000])
population = pd.Series([88550568, 89000000, 89500000])

# Calculate deaths per population
deaths_per_population_iran = total_deaths / population

# Calculate standard deviation
std_deviation = deaths_per_population_iran.std()

print(f"Standard Deviation of Deaths per Population: {std_deviation}")

