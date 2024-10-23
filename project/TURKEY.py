import pandas as pd
import matplotlib.pyplot as plt
# Load the data from the Excel file and only read specific lines
file_path = r'C:\Users\kimia\OneDrive\Documents/TURKEY.xlsx'  # Replace with your actual file path


data = pd.read_excel(file_path)
print(data)

total_deaths_turkey = pd.Series([102174, 110000, 120000])
population_turkey = pd.Series([86091691, 87000000, 87500000])

# Calculate deaths per population for Turkey
deaths_per_population_turkey = total_deaths_turkey / population_turkey

plt.figure(figsize=(20, 10))
plt.bar(data.iloc[:, 3], data.iloc[:, 8])
plt.xlabel('year')
plt.ylabel('total cases')
plt.title('Plot of Total cases per Year TURKEY')
plt.grid(True)
plt.show()