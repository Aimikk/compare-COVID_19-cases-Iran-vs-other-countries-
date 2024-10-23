import pandas as pd
import matplotlib.pyplot as plt
# Load the data from the Excel file and only read specific lines
file_path = r'C:\Users\kimia\OneDrive\Documents/DATA2.xlsx'  # Replace with your actual file path

total_deaths_usa = pd.Series([100000, 105000, 110000])
population_usa = pd.Series([331000000, 332000000, 333000000 ])

# Calculate deaths per population for the USA
deaths_per_population_usa = total_deaths_usa / population_usa
data = pd.read_excel(file_path)
print(data)

plt.figure(figsize=(20, 10))
plt.bar(data.iloc[:, 3], data.iloc[:, 8])
plt.xlabel('year')
plt.ylabel('total cases')
plt.title('Plot of Total cases per Year USA')
plt.grid(True)
plt.show()