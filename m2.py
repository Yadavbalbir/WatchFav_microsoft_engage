import pandas as pd 
import numpy as np 
import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

df1=pd.read_csv('tmdb_5000_credits.csv')
df2=pd.read_csv('tmdb_5000_movies.csv')

df1.columns = ['id','tittle','cast','crew']
df2= df2.merge(df1,on='id')

tfidf = TfidfVectorizer(stop_words='english')
df2['overview'] = df2['overview'].fillna('')
tfidf_matrix = tfidf.fit_transform(df2['overview'])

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
indices = pd.Series(df2.index, index=df2['title']).drop_duplicates()

def get_recommendations(title,num, cosine_sim=cosine_sim):
    # Get the index of the movie that matches the title
    idx = indices[title]

    # Get the pairwsie similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar movies
    sim_scores = sim_scores[1:(int(num)+1)]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]
    names=[]
    # Return the top 10 most similar movies
    a = np.array(df2[['title','id','runtime','vote_average', 'homepage','vote_count', 'overview']].iloc[movie_indices])
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

# print(get_recommendations("The Dark Knight", 10))

