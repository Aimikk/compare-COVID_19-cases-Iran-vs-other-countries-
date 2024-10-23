import pandas as pd
import matplotlib.pyplot as plt
# Load the data from the Excel file and only read specific lines
file_path = r'C:\Users\kimia\OneDrive\Documents/spain.xlsx'

data = pd.read_excel(file_path)
print(data)

plt.figure(figsize=(20, 10))
plt.bar(data.iloc[:, 3], data.iloc[:, 8])
plt.xlabel('year')
plt.ylabel('total cases')
plt.title('Plot of Total cases per Year Spain')
plt.grid(True)
plt.show()


total_deaths_spain = pd.Series([75000, 76000, 78000])
population_spain = pd.Series([47000000, 47100000, 47200000])


# Calculate deaths per population
deaths_per_population_spain = total_deaths_spain / population_spain

# Calculate standard deviation for Spain
std_deviation_spain = deaths_per_population_spain.std()

print(f"Standard Deviation of Deaths per Population in Spain: {std_deviation_spain}")