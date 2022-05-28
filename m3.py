import pandas as pd 
import numpy as np 
import requests
df1=pd.read_csv('tmdb_5000_credits.csv')
df2=pd.read_csv('tmdb_5000_movies.csv')

df1.columns = ['id','tittle','cast','crew']
df2= df2.merge(df1,on='id')


# Parse the stringified features into their corresponding python objects
from ast import literal_eval

features = ['cast', 'crew', 'keywords', 'genres']
for feature in features:
    df2[feature] = df2[feature].apply(literal_eval)

def get_director(x):
    for i in x:
        if i['job'] == 'Director':
            return i['name']
    return np.nan

def get_list(x):
    if isinstance(x, list):
        names = [i['name'] for i in x]
        #Check if more than 3 elements exist. If yes, return only first three. If no, return entire list.
        if len(names) > 3:
            names = names[:3]
        return names

    #Return empty list in case of missing/malformed data
    return []

df2['director'] = df2['crew'].apply(get_director)

features = ['cast', 'keywords', 'genres']
for feature in features:
    df2[feature] = df2[feature].apply(get_list)

df2[['title', 'cast', 'director', 'keywords', 'genres']].head(3)

def clean_data(x):
    if isinstance(x, list):
        return [str.lower(i.replace(" ", "")) for i in x]
    else:
        #Check if director exists. If not, return empty string
        if isinstance(x, str):
            return str.lower(x.replace(" ", ""))
        else:
            return ''

# Apply clean_data function to your features.
features = ['cast', 'keywords', 'director', 'genres']

for feature in features:
    df2[feature] = df2[feature].apply(clean_data)

def create_soup(x):
    return ' '.join(x['keywords']) + ' ' + ' '.join(x['cast']) + ' ' + x['director'] + ' ' + ' '.join(x['genres'])
df2['soup'] = df2.apply(create_soup, axis=1)

from sklearn.feature_extraction.text import CountVectorizer

count = CountVectorizer(stop_words='english')
count_matrix = count.fit_transform(df2['soup'])

from sklearn.metrics.pairwise import cosine_similarity

cosine_sim2 = cosine_similarity(count_matrix, count_matrix)
df2 = df2.reset_index()
indices = pd.Series(df2.index, index=df2['title'])

def get_recommendations(title,num, cosine_sim=cosine_sim2):
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
    a = np.array(df2[['title','id','runtime','vote_average', 'homepage', 'vote_count','overview']].iloc[movie_indices])
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
