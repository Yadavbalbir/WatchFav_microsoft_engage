from flask import Flask, render_template, request

# importing m1.py, m2.py, m3.py
import m1
import m2
import m3

# importing various movie category lists from tmdb_m.py
from tmdb_m import popular_movies, top_rated_movies, trending_movies_today, trending_movies_week

# importing various genre movies from tmdb_m.py
from tmdb_m import action_movies, drama_movies, romance_movies, family_movies, crime_movies, comedy_movies, scifi_movies, horror_movies
from tmdb_m import thriller_movies, adventure_movies, animation_movies

import requests
app = Flask(__name__)



##################### landing route ############################################
@app.route('/')
def landing_page():
    return render_template("landingpage.html")
#############################################################################

##################### home route ############################################


@app.route('/home')
def home():
    carosel_movies = []
    for i in range(0, 3):
        carosel_movies.append(trending_movies_today[i])
    return render_template(
        "home.html",
        carosel_movies=carosel_movies,
        trending_movies_today = trending_movies_today[:6],
        trending_movies_week = trending_movies_week[:6],
        popular_movies = popular_movies[:6],
        top_rated_movies = top_rated_movies[:6],
        action_movies = action_movies[:6],
        drama_movies = drama_movies[:6],
        romance_movies = romance_movies[:6],
        family_movies = family_movies[:6],
        crime_movies = crime_movies[:6],
        comedy_movies = comedy_movies[:6],
        scifi_movies = scifi_movies[:6],
        horror_movies = horror_movies[:6],
        thriller_movies = thriller_movies[:6],
        adventure_movies = adventure_movies[:6],
        animation_movies = animation_movies[:6]
    )
#############################################################################

################### similar_movies page route ###############################
@app.route('/similar_movies', methods=['POST'])
def similar_movies():
   if request.method == "POST":
      var = request.form["var"]
   
   if var=="action":
      movies=action_movies
   elif var == "drama":
      movies = drama_movies
   elif var == "romance":
      movies = romance_movies
   elif var == "family":
      movies = family_movies
   elif var == "crime":
      movies = crime_movies
   elif var == "comedy":
      movies = comedy_movies
   elif var == "sci-fi":
      movies = scifi_movies
   elif var == "horror":
      movies = horror_movies
   elif var == "thriller":
      movies = thriller_movies
   elif var == "adventure":
      movies = adventure_movies
   elif var == "animation":
      movies = animation_movies
   elif var == "popular":
      movies = popular_movies
   elif var == "top_rated":
      movies = top_rated_movies
   elif var == "t_today":
      movies = trending_movies_today
   elif var == "t_week":
      movies = trending_movies_today
   return render_template("similar_movies.html", movies=movies, var = var)
############################################################################


################### model1 route ###########################################
@app.route('/model1')
def model1():
    return render_template("model1.html")
############################################################################


################## model1 predict ###########################################
@app.route('/model1/predict', methods=["POST"])
def predict1():
    if request.method == "POST":
        num = request.form["num"]
    result = m1.recommend(int(num))
    return render_template("model1.html", result=result, num=num)
############################################################################


############## model2 route ###############################################
@app.route('/model2')
def model2():
    my_file = open("title.txt", "r")
    content = my_file.read()
    content_list = content.split("\n")
    my_file.close()
    return render_template("model2.html", contents=content_list)


@app.route('/model2/predict', methods=["POST"])
def predict2():
    if request.method == "POST":
        title = request.form["title"]
        num = request.form["num"]

    my_file = open("title.txt", "r")
    content = my_file.read()
    content_list = content.split("\n")
    my_file.close()
    if title not in content_list:
        result = 0
    else:
        result = m2.get_recommendations(title, int(num))
    return render_template("model2.html", result=result, num=num, title=title, contents=content_list)
##################################################################################################################


################# model3 route #####################################################################################
@app.route('/model3')
def model3():
    my_file = open("title.txt", "r")
    content = my_file.read()
    content_list = content.split("\n")
    my_file.close()
    return render_template("model3.html", contents=content_list)


@app.route('/model3/predict', methods=["POST"])
def predict3():
    if request.method == "POST":
        title = request.form["title"]
        num = request.form["num"]
    my_file = open("title.txt", "r")
    content = my_file.read()
    content_list = content.split("\n")
    my_file.close()
    if title not in content_list:
        result = 0
    else:
        result = m3.get_recommendations(title, int(num))
    return render_template("model3.html", result=result, num=num, title=title, contents=content_list)
########################################################################################################################


######################### Hybrid model route ###########################################################################
@app.route('/hybridmodel')
def model4():
    my_file = open("title.txt", "r")
    content = my_file.read()
    content_list = content.split("\n")
    my_file.close()
    return render_template("hybridmodel.html", contents=content_list)


@app.route('/hybridmodel/predict', methods=["POST"])
def predict4():
    if request.method == "POST":
        title = request.form["title"]
        num = request.form["num"]
    my_file = open("title.txt", "r")
    content = my_file.read()
    content_list = content.split("\n")
    my_file.close()
    if title not in content_list:
        result = 0
    else:
        result1 = m1.recommend(int(num))
        result2 = m2.get_recommendations(title, int(num))
        result3 = m3.get_recommendations(title, int(num))
        i = 0
        j = 0
        k = 0
        result = []
        title_only = []
        for n in range(0, (int(num))//3):
            while result3[i][0] in title_only:
                i = i+1
            result.append(result3[i])
            title_only.append(result3[i][0])
            while result2[j][0] in title_only:
                j = j+1
            result.append(result2[j])
            title_only.append(result2[j][0])
            while result1[k][0] in title_only:
                k = k+1
            result.append(result1[k])
            title_only.append(result1[k][0])
            i = i+1
            j = j+1
            k = k+1
        if int(num) % 3 == 1:
            while result3[i][0] in title_only:
                i = i+1
            result.append(result3[i])
            title_only.append(result3[i][0])
        if int(num) % 3 == 2:
            while result3[i][0] in title_only:
                i = i+1
            result.append(result3[i])
            title_only.append(result3[i][0])
            while result2[j][0] in title_only:
                j = j+1
            result.append(result2[j])
            title_only.append(result2[j][0])

    return render_template("hybridmodel.html", result=result, num=num, title=title, contents=content_list)
###########################################################################################################


####################### movie page routing #######################################################################
@app.route('/movie', methods=['POST'])
def movie():
    if request.method == "POST":
        title = request.form["title"]
        id = request.form["id"]
        runtime = request.form["runtime"]
        rating = request.form["rating"]
        ott = request.form["ott"]
        poster = request.form["poster"]
        vote = request.form["vote"]
        overview = request.form["overview"]
        backdrop = request.form["backdrop"]

    response_recommend = requests.get("https://api.themoviedb.org/3/movie/"+str(id)+"/recommendations?api_key=8392ec73124468f81442d4565edccad7&language=en-US&page=1")
    recommend = response_recommend.json()
    if "status_code" not in recommend:
        list_recommend = recommend['results']
        recommended_movies = []
        length = 6
        if length > len(list_recommend):
            length = len(list_recommend)
        for i in range(0, length):
            arr = []
            arr.append(list_recommend[i]['title'])
            arr.append(list_recommend[i]['id'])
            arr.append(list_recommend[i]['release_date'])
            arr.append(list_recommend[i]['vote_average'])
            url = "https://www.themoviedb.org/movie/" + \
                str(list_recommend[i]['id'])+"/watch"
            path = "https://image.tmdb.org/t/p/original" + \
                list_recommend[i]['poster_path']
            arr.append(url)
            arr.append(path)
            arr.append(list_recommend[i]['vote_count'])
            arr.append(list_recommend[i]['overview'])
            backdrop_path = "https://image.tmdb.org/t/p/original" + \
                list_recommend[i]['backdrop_path']
            arr.append(backdrop_path)
            recommended_movies.append(arr)
    else:
        recommended_movies = []

    return render_template(
            'movie.html', 
            title = title, 
            id = id, 
            runtime = runtime, 
            rating = rating, 
            ott = ott, 
            poster = poster, 
            vote = vote, 
            overview = overview, 
            backdrop = backdrop, 
            popular_movies=popular_movies[:6],
            top_rated_movies=top_rated_movies[:6],
            trending_movies_today=trending_movies_today[:6],
            trending_movies_week=trending_movies_week[:6],
            recommended_movies = recommended_movies
         )
###############################################################################################################


if __name__ == '__main__':
    app.run(debug=True)
