import pandas as pd

from matplotlib import pyplot as plt

df = pd.read_csv('netflix_titles.csv')

director_count = df['director'].value_counts()

top_20_director = director_count.head(20)

plt.figure(figsize=(12, 8))
top_20_director.plot(kind='bar')
plt.title('Top 20 directori - per numar filme produse')
plt.xlabel('Director')
plt.ylabel('Numar filme')
plt.xticks(rotation=45)
plt.show()