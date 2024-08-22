import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('car_sales.csv')

# Data Exploration
print(df.head())
print(df.info())

# Data Cleaning (if needed)

# Data Analysis
total_sales = df['Sales'].sum()
average_price = df['Price'].mean()
most_popular_model = df['Model'].value_counts().idxmax()

# Data Visualization
plt.figure(figsize=(10, 6))
plt.bar(df['Model'], df['Sales'])
plt.xlabel('Car Model')
plt.ylabel('Sales')
plt.title('Car Sales by Model')
plt.xticks(rotation=90)
plt.show()

# Drawing Insights
print(f'Total Sales: ${total_sales}')
print(f'Average Price: ${average_price:.2f}')
print(f'Most Popular Car Model: {most_popular_model}')

# Presentation: Explain your findings and insights in a clear and organized manner.