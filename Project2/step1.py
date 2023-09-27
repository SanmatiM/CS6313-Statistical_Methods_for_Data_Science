import pandas as pd

# Define the URL to the CSV file
csv_file_url = "https://raw.githubusercontent.com/SanmatiM/CS6313-Statistical_Methods_for_Data_Science/master/Project2/population_dataset.csv"

# Read the CSV data directly from the URL using Pandas
data = pd.read_csv(csv_file_url)

# Calculate statistics using Pandas
n = len(data)
min_value = data.min().values[0]
max_value = data.max().values[0]
mean_value = data.mean().values[0]
q25 = data.quantile(0.25).values[0]
q75 = data.quantile(0.75).values[0]
iqr_value = q75 - q25
lower_outlier_limit = q25 - 1.5 * iqr_value
upper_outlier_limit = q75 + 1.5 * iqr_value
outliers = len(data[(data < lower_outlier_limit) | (data > upper_outlier_limit)])

# Output the results
print("STEP1 RESULTS ON POPULATION DATASET")
print("Length:", n)
print("Minimum:", min_value)
print("Maximum:", max_value)
print("Mean:", mean_value)
print("25% Quartile:", q25)
print("75% Quartile:", q75)
print("Interquartile Range:", iqr_value)
print("Lower Outlier Limit:", lower_outlier_limit)
print("Upper Outlier Limit:", upper_outlier_limit)
print(outliers, "outliers found.")
