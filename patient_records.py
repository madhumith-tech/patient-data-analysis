import pandas as pd

# Read the dataset
df = pd.read_csv('patient_records.csv')

# Display first 5 rows
print(df.head())

# Display column names
print(df.columns)

# Maximum cholesterol for each age
print(df.groupby('age')['cholesterol'].max())

# Patients with cholesterol > 250 and weight > 250
print(df[(df['cholesterol'] > 250) & (df['weight'] > 250)])

# Average cholesterol
average = df['cholesterol'].mean()

# Patient IDs with cholesterol above average
print(df[df['cholesterol'] > average]['patient_id'])

# Sort by cholesterol from highest to lowest
print(df.sort_values('cholesterol', ascending=False))

# Create cholesterol per weight column
df['chol_per_weight'] = df['cholesterol'] / df['weight']

print(df)