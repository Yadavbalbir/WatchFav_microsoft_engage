# WatchFav : Movie Recommendation Webapp

### WatchFav is a web application which consist of different Algorithms and API calls that recommend movies, build as a solution of 3rd challenge to the Microsoft Engage 2022 program

<!-- #### Demo video link : 
#### Hosted web application :  -->



<img width="1432" alt="landing" src="screenshots\landing_intro.png">


### 📌 Table of Contents
* [Features](#topfeatures)
* [Features](#efeatures)
* [Tech Stack Used/ Dependencies](#tech-stack)
* [Timeline](#timeline)
* [Getting Started/ Setup](#getting-started)
* [Usage Guide/ Application flow](#usage)
* [Challenges faced and learnings](#challenges)
* [Future Scope/ What's next?](#scope)
* [Resources](#resources)



<a id="topfeatures"></a>
## 🚀 Main Features
- Get Recommended Movies based on different algorithms and approaches.
- Latest Trending Movies
- Top Rated Movies
- Popular Movies
- Get Direct Access to OTT Links having that particular movie

<img width="1432" alt="landing" src="screenshots\main_features.png">

<a id="efeatures"></a>
## 🚀 Essential Features
- Dynamic interactive simple and attractive UI.
- Real time posters and banner fatched corresponding to each movie using TMDB API
- 3 Carousel at home page showing top 3 movies trending today in real time using TMDB API. 
- Watch latest trending movies Today.
- Watch latest trending movies This.
- Popular movies and top rated movies
- View real time movies rating, release day, duration.
- Get to see overview about movie on movie player page. 
- View and watch movies popular in every genre sorted using sorting algorithms. 
- Get list of movies based on it's genre by clicking movie more
- Get direct link to the page where shows movies availability at different OTT platforms.
- Get Recommended movies based on what you are watching now
- Separate page to check different algorithms and get number of recommended movies with what you fill in form. 
- [Add more features](#feature-request)...


<a id="tech-stack"></a>
## 💻 Tech Stack Used/ Dependencies

<img src = "https://img.shields.io/badge/-Stackoverflow-FE7A16?style=for-the-badge&logo=stack-overflow&logoColor=white"><img src = "https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white"><img src = "https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white"><img src = "https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white"><img src = "https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white"><img src = "https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white"><img src = "https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white"><img src = "https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E"><img src = "https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white"><img src = "https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white"><img src = "https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"><img src = "https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white"><img src = "https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white"><img src = "https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white"><img src = "https://img.shields.io/badge/SciPy-%230C55A5.svg?style=for-the-badge&logo=scipy&logoColor=%white"><img src = "https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white">


<a id="timeline"></a>
## ⚡️ WatchFav Timeline

I'm being student from mechanical engineering having knowledge of basic DSA and enthusiasm for software development. It has been first ever project for me that is build end-to-end right from scratch. It wasn't possible without consistent & punctual daily routines. It has been one of the best learning experiences I encounter till now where I have learned so many tech stacks and not only learned but implemented as well. 

Here is 4-week consisted timeline what is followed to build this project.

<img width="1432" alt="landing" src="screenshots\timeline.png">





<a id="getting-started"></a>
## 📦 Getting Started/ Setup

1. Clone this repository.

```javascript
  git clone https://github.com/Yadavbalbir/WatchFav_microsoft_engage.git
```  

2. Head over to project directory and install dependencies by running the following in terminal.

```javascript
   pip install -r requirements.txt
```

3. To start this app run the following command in terminal in project directory

```javascript
  python app.py
```

4. If requirements.txt throws error then run the following commands in the terminal

```javascript
  pip install flask
  pip install pandas
  pip install requests
  pip install sklearn
```

5. Now run the app again
```javascript
  python app.py
```
  
5. App will run on `http://127.0.0.1:5000/`, so click it and head over to browser to view web app.


<a id="usage"></a>
## 📖 Usage guide/ Application flow

Visit the hosted web application at "link"


## Landing Page 

This page consists details about the project like features, timeline, algorithms and approaches. This is **not** our home page of the project. 

Click **Get Started** to enter in our main project

<img width="1432" alt="landing page" src="screenshots\Landing_with_annotation.png">

## Home Page 
Once we click Get Started, we will enter into the home page of our project. which consists the following things

- ### Carousel having trending movies today
    <img width="1436" alt="carousel" src="screenshots\homepage_carousel.png">

- ### Popular Movies 
    <img width="1436" alt="carousel" src="screenshots\popular_movies.png">

- ### Top Rated Movies 
    <img width="1436" alt="carousel" src="screenshots\top_rated.png">

- ### Today's Trending Movies 
    <img width="1436" alt="carousel" src="screenshots\trending_today.png">

- ### This week Trending Movies 
    <img width="1436" alt="carousel" src="screenshots\trending_week.png">

- ### popular in action Movies
    <img width="1436" alt="carousel" src="screenshots\popular_action.png">

- ### popular in Drama Movies 
    <img width="1436" alt="carousel" src="screenshots\popular_drama.png">

Similarily we have popular movies corressponding to each and every genre. If you want to see more movies than the limited movies shown on home page then click to **see more**. You will land the website which have same category movies which you wanted to see. 

**Let's see more Horror Movies**
<img width="1436" alt="carousel" src="screenshots\see_more.png">

**Results of see more Horror Movies**
<img width="1436" alt="carousel" src="screenshots\result_see_more.png">



## Movie Page

Now let's click **watch now** at one of the movies shown on our website
<img width="1436" alt="carousel" src="screenshots\watch_now.png">

Once you click watch now,  you'll land on movie page consisting the dummy video player but real **title**, **overview**, **OTT Link**, **rating**, **vote count**, **release_date or duration in mins**, **language**. 
This is how it look like
<img width="1436" alt="carousel" src="screenshots\watch_thor_not_annotated.png">

Annotated img
<img width="1436" alt="carousel" src="screenshots\watch_thor.png">


Now scroll down on this page you will see **Recommended for you** section which consists of movies recommended based on watch you are watching now. 

<img width="1436" alt="carousel" src="screenshots\recommended_for_thor.png">



## separate pages for testing different models

- ### Test page for Model-1
    this is how our model-1 webpage looklike. You can enter any number of movies you want, It will give the results based on weighted Avag and sorted with sorting algorithms to get the movies with highest weighted avag movie at the top

    <img width="1436" alt="carousel" src="screenshots\weighted_avg.png">

    Now Let's enter 10 in the form input and hit **Recommend** button
    These are results of top movies in our database sorted with sorting algorithms

    <img width="1436" alt="carousel" src="screenshots\result_model-1.png">
    
- ### Test Webpage for our model-2
    this is how our model-2 webpage look like. You have to enter the title of movie watching or watched and number of movies you want in recommendation. It is based on **TF*TDF** and **Cosine_similarity** algorithms. in model-2 we consider **overview** of movies to apply our algorithms and then sort the results

     <img width="1436" alt="carousel" src="screenshots\model-2.png">

     Now let's enter title : "Avengers: Age of Ultron"
                     Number : 5
    these are the top 5 recommended movies for Avengers look like

     <img width="1436" alt="carousel" src="screenshots\result_model-2.png">

- ### Test webpage for our model-3
    same approach as above. more details are available on webpage

- ### Test webpage for our hybrid-4
    same as above. more details are available on webpage

<a id="scope"></a>
## 🚧 Future Scope/ What's next?

- [ ] Adding user authentication.
- [ ] User Dashboard showing users activity
- [ ] Add to favourite button on movies which will add movies in users dashboard
- [ ] Watch Later
- [ ] Collobrate filtering with the different users available on our website


<a id="resources"></a>
## 📚 Resources

- [Bootstrap](https://getbootstrap.com/)
- [HTML](https://www.w3schools.com/html/default.asp)
- [CSS](https://www.w3schools.com/css/default.asp)
- [python](https://docs.python.org/3/)
- [Flask](https://flask.palletsprojects.com/en/2.1.x/)
- [Heroku Documentation](https://devcenter.heroku.com/categories/reference)
