import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the Excel file
file_path = r'C:\Users\kimia\OneDrive\Documents\DATA.xlsx'  # Replace with your actual file path
data = pd.read_excel(file_path)

# Print the data (optional)
print(data)

# Plotting total cases per year for IRI
plt.figure(figsize=(20, 10))
plt.bar(data.iloc[:, 3], data.iloc[:, 8])  # Adjust columns as per your dataset
plt.xlabel('Year')
plt.ylabel('Total Cases')
plt.title('Plot of Total Cases per Year in IRI')
plt.grid(True)
plt.show()

# Accurate data for Iran (replace with actual values)
total_deaths_iran = pd.Series([140000, 145000, 150000])
population_iran = pd.Series([87723443, 88000000, 88200000])

# Calculate deaths per population for Iran
deaths_per_population_iran = total_deaths_iran / population_iran

# Calculate standard deviation
std_deviation_iran = deaths_per_population_iran.std()
print(f"Standard Deviation of Deaths per Population in Iran: {std_deviation_iran}")


