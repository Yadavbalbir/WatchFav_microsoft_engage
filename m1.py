# importing libraries and packages
import pandas as pd 
import numpy as np 
import requests

# Reading csv dataset using pandas
df1=pd.read_csv('tmdb_5000_credits.csv')
df2=pd.read_csv('tmdb_5000_movies.csv')

# Merging two dataset into df2
df1.columns = ['id','tittle','cast','crew']
df2= df2.merge(df1,on='id')

# Builing weighted average model 
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

# Recommend function which takes a number as a input and shows output
# Returns a 2D array containg song title, id, runtime, vote_average and website url
def recommend(num):
    names = []
    a= np.array(q_movies[['title','id','runtime','vote_average', 'homepage', 'vote_count', 'overview']].head(int(num)))
    for n in a:
        arr = []
        arr.append(n[0])
        arr.append(n[1])
        arr.append(n[2])
        arr.append(n[3])
        arr.append(n[4])
        response = requests.get('https://api.themoviedb.org/3/movie/'+str(arr[1])+'?api_key=8392ec73124468f81442d4565edccad7&language=en-US')
        data = response.json()
        path ="https://image.tmdb.org/t/p/original" + data['poster_path']
        arr.append(path)
        arr[4] = "https://www.themoviedb.org/movie/"+str(arr[1])+"/watch"
        arr.append(n[5])
        arr.append(n[6])
        backdrop = "https://image.tmdb.org/t/p/original" + data['backdrop_path']
        arr.append(backdrop)
        names.append(arr)
   
    return names



