import codecademylib3
import pandas as pd

df = pd.read_csv('imdb.csv')

df.rename(columns={
  'name': 'movie_title'
},
inplace=True
)

print(df)