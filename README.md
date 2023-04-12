# WatchMovie- Movie Recommendation system


## Overview

This web app provides movie recommendations based on user preferences and movie similarity, it offers generalized recommendations based on movie popularity, genre, and year as well as recommend movies using content-based filtering based on user's selection. It uses the TMDB_5000 dataset and is built with Flask and JavaScript.

## Features

1. Most popular movies based on different genres. 
2. Most popular movies based on different years. 
3. Recommended movies similar to the user's selected movie.
4. Detailed movie information and trailer linked for each movie.

## Interface

**Landing page**

- Landing page to get started

![landing page](/static/images/img1.png)


-User can search movie and get suggestions of movies based on input characters.

![landing page](/static/images/img2.png)

**Movie page**
- The user can access detailed information and trailers of their selected movie on this page. 
- Additionally, it also provides recommendations of similar movies based on the user's chosen movie.

![landing page](/static/images/img3.png)

![landing page](/static/images/img4.png)

**Recommendations page**
- It recommends most popular movies based on different genres and years.

![landing page](/static/images/img6.png)


![landing page](/static/images/img7.png)


![landing page](/static/images/img8.png)


![landing page](/static/images/img9.png)


## Tech Stack 
**Tech Stack:**

- Backend: Python, Flask
- Frontend: HTML, CSS, JavaScript, BootStrap, jQuery
- Machine Learning: scikit-learn, pandas, numpy, ast
- Database: SQLite

**Software Used:**

- IDE: Visual Studio Code
- Git: GitHub
- API: The Movie Database API (TMDB)

## Installation

1. Clone the repository in your local system: git clone https://github.com/webdesign4u-html5/MovieRecommendation.git
2. Navigate to the project directory: cd your-repo
3. Make sure Python is installed and updated in your system.
4. Create a virtual environment: python -m venv env
5. Activate the virtual environment:
    - On Windows: source env/Scripts/activate
    - On macOS and Linux: source env/bin/activate
6. Install the required packages: pip install -r requirements.txt
7. Run the app: python app.py or py app.py
8. Open the app in your web browser at "http://127.0.0.1:5000"

## Dataset

This app uses the TMDB_5000 dataset, which can be found on [Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata).
