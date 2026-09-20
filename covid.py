# pip install pandas matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Sample data - Original dataset ki Our World in Data csv download chey
# csv link: https://covid.ourworldindata.org/data/owid-covid-data.csv
data = {
    'location': ['USA', 'India', 'Brazil', 'UK', 'France', 'Russia', 'USA'],
    'total_cases': [1000000, 900000, 800000, 700000, 600000, 500000, 1000000]
}
df = pd.DataFrame(data)

# Top 5 countries by total cases
# Real dataset lo: df.groupby('location')['total_cases'].max().sort_values...
top5 = df.sort_values(by='total_cases', ascending=False).drop_duplicates('location').head(5)
print(top5)

# Plot bar chart
plt.figure(figsize=(8,5))
plt.bar(top5['location'], top5['total_cases'], color='red')
plt.title('Top 5 Countries by Total Cases')
plt.xlabel('Country')
plt.ylabel('Total Cases')
plt.show()