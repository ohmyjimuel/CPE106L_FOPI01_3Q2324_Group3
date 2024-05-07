import pandas as pd
import matplotlib.pyplot as plt

# Load the data set
data = pd.read_csv('breadprice.csv')

# Clean the data set
data = data.drop(data.columns[[0]], axis=1)
data = data.apply(pd.to_numeric, errors='coerce') 
data = data.dropna(axis=1, how='all')
data = data.fillna(method='ffill', axis=0)

# Calculate the average price for each year
average_prices = data.mean(axis=1)

# Create a line plot
years = range(2012, 2023)
plt.plot(years, average_prices)
plt.xlabel('Year')
plt.ylabel('Average Price')
plt.title('Average Bread Price by Year')
plt.show()
