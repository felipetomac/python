import codecademylib3
import pandas as pd

df = pd.read_csv('imdb.csv')

df.columns = ['ID','Title','Category','Year Released','Rating']

print(df)