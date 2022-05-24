

# path = "https://image.tmdb.org/t/p/w500"+ data["poster_path"]

# print(path)

import pandas as pd 
import numpy as np 
df1=pd.read_csv('tmdb_5000_credits.csv')
df2=pd.read_csv('tmdb_5000_movies.csv')

df1.columns = ['id','tittle','cast','crew']
df2= df2.merge(df1,on='id')
C= df2['vote_average'].mean()
m= df2['vote_count'].quantile(0.9)
q_movies = df2.copy().loc[df2['vote_count'] >= m]

def weighted_rating(x, m=m, C=C):
    v = x['vote_count']
    R = x['vote_average']
    # Calculation based on the IMDB formula
    return (v/(v+m) * R) + (m/(m+v) * C)


q_movies['score'] = q_movies.apply(weighted_rating, axis=1)
q_movies = q_movies.sort_values('score', ascending=False)


def recommend(num):
    names = []
    a= np.array(q_movies[['title','id','runtime']].head(int(num)))
    for n in a:
        names.append(n)
    return names

a= recommend(10)

for A in a:
    print(A[0])
    print(A[1])
    print(A[2])

