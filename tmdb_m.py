import requests

# Function to get movies on particular genre based on genre_id
def get_genre_movies(genre_id):
    response = requests.get("https://api.themoviedb.org/3/discover/movie?api_key=8392ec73124468f81442d4565edccad7&with_genres="+str(genre_id)+"&page=1")
    response_json=response.json()
    list_genre= response_json['results']
    movies = []
    for i in range(0, len(list_genre)):
        arr = []
        arr.append(list_genre[i]['title'])
        arr.append(list_genre[i]['id'])
        arr.append(list_genre[i]['release_date'])
        arr.append(list_genre[i]['vote_average'])
        url = "https://www.themoviedb.org/movie/"+str(list_genre[i]['id'])+"/watch"
        path = "https://image.tmdb.org/t/p/original"+ list_genre[i]['poster_path']
        arr.append(url)
        arr.append(path)
        arr.append(list_genre[i]['vote_count'])
        arr.append(list_genre[i]['overview'])
        backdrop = "https://image.tmdb.org/t/p/original" + list_genre[i]['backdrop_path']
        arr.append(backdrop)
        arr.append(list_genre[i]['popularity'])
        movies.append(arr)
    return movies


# fetching popular movies from TMDB using TMDB api
response_popular = requests.get("https://api.themoviedb.org/3/movie/popular?api_key=8392ec73124468f81442d4565edccad7&language=en-US&page=1")
popular=response_popular.json()
list_popular = popular['results']

# fetching top rated movies from TMDB using TMDB api
response_top_rated = requests.get("https://api.themoviedb.org/3/movie/top_rated?api_key=8392ec73124468f81442d4565edccad7&language=en-US&page=1")
top_rated=response_top_rated.json()
list_top_rated= top_rated['results']

# fetching today's trending movies from TMDB using TMDB api
response_trending_today = requests.get("https://api.themoviedb.org/3/trending/all/day?api_key=8392ec73124468f81442d4565edccad7")
trending_today=response_trending_today.json()
list_trending_today= trending_today['results']

# fetching this week's trending movies from TMDB using TMDB api
response_trending_week = requests.get("https://api.themoviedb.org/3/trending/all/week?api_key=8392ec73124468f81442d4565edccad7")
trending_week=response_trending_week.json()
list_trending_week= trending_week['results']


# collecting popular movies details in 2D list
popular_movies = []
for i in range(0, len(list_popular)):
    arr = []
    arr.append(list_popular[i]['title'])
    arr.append(list_popular[i]['id'])
    arr.append(list_popular[i]['release_date'])
    arr.append(list_popular[i]['vote_average'])
    url = "https://www.themoviedb.org/movie/"+str(list_popular[i]['id'])+"/watch"
    path = "https://image.tmdb.org/t/p/original"+ list_popular[i]['poster_path']
    arr.append(url)
    arr.append(path)
    arr.append(list_popular[i]['vote_count'])
    arr.append(list_popular[i]['overview'])
    backdrop = "https://image.tmdb.org/t/p/original" + list_popular[i]['backdrop_path']
    arr.append(backdrop)
    popular_movies.append(arr)

#collecting top_rated_movies details in 2D list
top_rated_movies = []
for i in range(0, len(list_top_rated)):
    arr = []
    arr.append(list_top_rated[i]['title'])
    arr.append(list_top_rated[i]['id'])
    arr.append(list_top_rated[i]['release_date'])
    arr.append(list_top_rated[i]['vote_average'])
    url = "https://www.themoviedb.org/movie/"+str(list_top_rated[i]['id'])+"/watch"
    path = "https://image.tmdb.org/t/p/original"+ list_top_rated[i]['poster_path']
    arr.append(url)
    arr.append(path)
    arr.append(list_top_rated[i]['vote_count'])
    arr.append(list_top_rated[i]['overview'])
    backdrop = "https://image.tmdb.org/t/p/original" + list_top_rated[i]['backdrop_path']
    arr.append(backdrop)
    top_rated_movies.append(arr)

#collecting today's trending movies details in 2D list
trending_movies_today = []
for i in range(0, len(list_trending_today)):
    arr = []
    if "title" in list_trending_today[i]:
        arr.append(list_trending_today[i]['title'])
    elif "original_title" in list_trending_today[i]:
        arr.append(list_trending_today[i]['original_title'])
    elif "name" in list_trending_today[i]:
        arr.append(list_trending_today[i]['name'])
    elif "original_name" in list_trending_today[i]:
        arr.append(list_trending_today[i]['original_name'])
    else:
        continue
    arr.append(list_trending_today[i]['id'])

    if "release_date" in list_trending_today[i]:
        arr.append(list_trending_today[i]['release_date'])
    elif "first_air_date" in list_trending_today[i]:
        arr.append(list_trending_today[i]['first_air_date'])
    else:
        continue

    
    arr.append(list_trending_today[i]['vote_average'])
    url = "https://www.themoviedb.org/movie/"+str(list_trending_today[i]['id'])+"/watch"
    path = "https://image.tmdb.org/t/p/original"+ list_trending_today[i]['poster_path']
    arr.append(url)
    arr.append(path)
    arr.append(list_trending_today[i]['vote_count'])
    arr.append(list_trending_today[i]['overview'])
    backdrop = "https://image.tmdb.org/t/p/original" + list_trending_today[i]['backdrop_path']
    arr.append(backdrop)
    trending_movies_today.append(arr)

#collecting weekly trending movies in 2D list
trending_movies_week = []
for i in range(0, len(list_trending_week)):
    arr = []
    #appending title in arr
    if "title" in list_trending_week[i]:
        arr.append(list_trending_week[i]['title'])
    elif "original_title" in list_trending_week[i]:
        arr.append(list_trending_week[i]['original_title'])
    elif "name" in list_trending_week[i]:
        arr.append(list_trending_week[i]['name'])
    elif "original_name" in list_trending_week[i]:
        arr.append(list_trending_week[i]['original_name'])
    else:
        continue

    arr.append(list_trending_week[i]['id'])

    # appending release_date or first_air_date
    if "release_date" in list_trending_week[i]:
        arr.append(list_trending_week[i]['release_date'])
    elif "first_air_date" in list_trending_week[i]:
        arr.append(list_trending_week[i]['first_air_date'])
    else:
        continue

    arr.append(list_trending_week[i]['vote_average'])
    url = "https://www.themoviedb.org/movie/"+str(list_trending_week[i]['id'])+"/watch"
    path = "https://image.tmdb.org/t/p/original"+ list_trending_week[i]['poster_path']
    arr.append(url)
    arr.append(path)
    arr.append(list_trending_week[i]['vote_count'])
    arr.append(list_trending_week[i]['overview'])
    backdrop = "https://image.tmdb.org/t/p/original" + list_trending_week[i]['backdrop_path']
    arr.append(backdrop)
    trending_movies_week.append(arr)



######################################### Genre id with Genre #############################################################
#       28    : Action
#       18    : Drama 
#       10749 : Romance 
#       10751 : Family
#       80    : Crime 
#       35    : Comedy 
#       878   : Sci-Fi 
#       27    : Horror 
#       53    : Thriller 
#       12    : adventure 
#       16    : Animation 
#       99    : Documentary 
#       10752 : War

###########################################################################################################################

# collecting movies with genre action & sorting based on it's popularity in 2D list
action_movies = get_genre_movies(28)                                     
action_movies.sort(key = lambda x: x[9], reverse=True)             ## sorting

# collecting movies with genre Drama & sorting based on it's popularity in 2D list
drama_movies = get_genre_movies(18)  
drama_movies.sort(key=lambda x:x[9], reverse=True)                 ## sorting    

# collecting movies with genre Romance & sorting based on it's popularity in 2D list
romance_movies = get_genre_movies(10749)  
romance_movies.sort(key=lambda x:x[9], reverse=True)                 ## sorting  

# collecting movies with genre Family & sorting based on it's popularity in 2D list
family_movies = get_genre_movies(10751)  
family_movies.sort(key=lambda x:x[9], reverse=True)                 ## sorting  

# collecting movies with genre Crime & sorting based on it's popularity in 2D list
crime_movies = get_genre_movies(80)  
crime_movies.sort(key=lambda x:x[9], reverse=True)                 ## sorting         

# collecting movies with genre Comedy & sorting based on it's popularity in 2D list
comedy_movies = get_genre_movies(35)  
comedy_movies.sort(key=lambda x:x[9], reverse=True)                 ## sorting

# collecting movies with genre Sci-Fi & sorting based on it's popularity in 2D list
scifi_movies = get_genre_movies(878)  
scifi_movies.sort(key=lambda x:x[9], reverse=True)                 ## sorting

# collecting movies with genre Horror & sorting based on it's popularity in 2D list
horror_movies = get_genre_movies(27)  
horror_movies.sort(key=lambda x:x[9], reverse=True)                 ## sorting

# collecting movies with genre Thriller & sorting based on it's popularity in 2D list
thriller_movies = get_genre_movies(53)  
thriller_movies.sort(key=lambda x:x[9], reverse=True)                 ## sorting

# collecting movies with genre Adventure & sorting based on it's popularity in 2D list
adventure_movies = get_genre_movies(12)  
adventure_movies.sort(key=lambda x:x[9], reverse=True)                 ## sorting

# collecting movies with genre Animation & sorting based on it's popularity in 2D list
animation_movies = get_genre_movies(16)  
animation_movies.sort(key=lambda x:x[9], reverse=True)                 ## sorting