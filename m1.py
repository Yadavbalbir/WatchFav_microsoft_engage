import pandas as pd 
import numpy as np 
import requests

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
    a= np.array(q_movies[['title','id','runtime','vote_average', 'homepage']].head(int(num)))
    for n in a:
        names.append(n)

    for n in names:
        response = requests.get('https://api.themoviedb.org/3/movie/'+str(n[1])+'?api_key=8392ec73124468f81442d4565edccad7&language=en-US')
        data = response.json()
        n[4]="https://www.themoviedb.org/movie/"+str(n[1])+"/watch"
    return names


# print(recommend(5))

