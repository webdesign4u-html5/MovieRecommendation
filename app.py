import pandas as pd
from flask import Flask, render_template, jsonify, request
import sqlite3
import requests
from content_based import get_recommendations

app =Flask(__name__)

def db_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect("./model/"+db_name+".sqlite")
    except sqlite3.error as e:
        print(e)
    return conn



conn = db_connection("dataset")
cursor = conn.cursor()
cursor.execute("Select * from dataset")
movies_result = cursor.fetchall()
conn.close()


@app.route('/')
def index():
     return render_template('index.html')

# Recommendation page by genre and by year
@app.route('/selection')
def selection():
    genre_movies=[]
    genre_posters=[]
    year_movies=[]
    year_posters=[]
    return render_template('selection.html', genre_movies=genre_movies, genre_posters=genre_posters, year_movies=year_movies, year_posters=year_posters)



def fetchPoster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data =response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path'] 

def fetchTrailer(movie_id):
    # Make the API request
    url = f'https://api.themoviedb.org/3/movie/{movie_id}/videos'
    params = {'api_key': '8265bd1679663a7ea12ac168da84d2e8', 'language': 'en-US'}
    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code != 200:
        raise Exception(f"Failed to fetch trailer for movie {movie_id}: {response.text}")

    # Extract the trailer key from the response
    data = response.json()
    for video in data['results']:
        if video['type'] == 'Trailer':
            return video['key']

    # If no trailer was found, return None
    return None


# Suggestion by Genre
def byGenre(genre):
    counter=0
    genre_movies=[]
    genre_posters=[]

    conn = db_connection("popular")
    cursor =conn.cursor()
    cursor.execute("Select movie_id, genres from popular")
    results =cursor.fetchall()

    for row in results:
        if counter!=6:
            mov_gen= list(row[1].split("$"))
            for gen in mov_gen:
                if gen==genre:
                    cursor.execute("Select title from popular where movie_id = '"+str(row[0])+"'")
                    title=cursor.fetchall()
                    genre_movies.append(title[0][0])
                    genre_posters.append(fetchPoster(row[0]))
                    counter += 1
                    break
        else:
            break

    return genre_movies, genre_posters


@app.route('/getByGenre' , methods=['GET','POST'])
def getByGenre():
    genre = request.form["genre"]
    genre_movies, genre_posters = byGenre(genre)
    response = jsonify(
        {"genre_movies": genre_movies}, {"genre_posters": genre_posters}
    )
    return response


# suggestions by year
def byYear(year):
    counter=0
    year_movies=[]
    year_posters=[]

    conn = db_connection("popular")
    cursor =conn.cursor()
    cursor.execute("Select movie_id, release_date from popular")
    results =cursor.fetchall()

    for row in results:
        if counter!=6:
            if year==row[1]:
                cursor.execute("Select title from popular where movie_id = '"+str(row[0])+"'")
                title=cursor.fetchall()
                year_movies.append(title[0][0])
                year_posters.append(fetchPoster(row[0]))
                counter += 1
        else:
            break

    return year_movies, year_posters

@app.route('/getByYear', methods=['GET', 'POST'])
def getByYear():
    year= request.form["year"]
    year_movies, year_posters = byYear(year)
    response = jsonify(
        {"year_movies": year_movies}, {"year_posters": year_posters}
    )
    return response



# Autocomplete Suggestions of movies to search bar
@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    search = request.args.get('search')
    conn = db_connection("dataset")
    cursor = conn.cursor()
    cursor.execute("SELECT title FROM dataset WHERE title LIKE ? LIMIT 10", ('%' + search + '%',))
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(results)



# Movie page
@app.route('/movie/<movie_name>', methods=['GET'])

def movie(movie_name):
   recommendations,idx=get_recommendations(movie_name) 
   for row in movies_result:
        if row[2] == movie_name:
            movie_idx = row[0]
            movie_id = row[1]
            break;
   trailer_key = fetchTrailer(movie_id)
   movie_poster = fetchPoster(movie_id)

   movie_posters = []
   recommended_movies = []
   for i,j in zip(recommendations, idx):
       recommended_movies.append(i)
       movie_posters.append(fetchPoster(j))
   mov_genre=[]
   mov_cast=[]
   for row in movies_result:
        mg = list(row[5].split("$"))
        mov_genre.append(mg)
        mc = list(row[7].split("$"))
        mov_cast.append(mc)
   return render_template('recommendation.html',mov_genre=mov_genre,mov_cast=mov_cast, movie_idx=movie_idx, movies_result=movies_result,movie_poster=movie_poster, trailer_key=trailer_key, recommended_movies=recommended_movies, movie_posters= movie_posters )



if __name__=="__main__":
    app.run(debug=True)