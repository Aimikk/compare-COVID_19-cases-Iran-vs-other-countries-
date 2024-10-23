import pandas as pd
import matplotlib.pyplot as plt
# Load the data from the Excel file and only read specific lines
file_path = r'C:\Users\kimia\OneDrive\Documents/s.korea.xlsx'  # Replace with your actual file path

total_deaths_korea = pd.Series([35934, 36000, 36500])
population_korea = pd.Series([51717590, 51858482, 51800000])

# Calculate deaths per population for South Korea
deaths_per_population_korea = total_deaths_korea / population_korea

data = pd.read_excel(file_path)
print(data)

plt.figure(figsize=(20, 10))
plt.bar(data.iloc[:, 3], data.iloc[:, 8])
plt.xlabel('year')
plt.ylabel('total cases')
plt.title('Plot of Total cases per Year KOREA')
plt.grid(True)
plt.show()