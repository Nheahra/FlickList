import random

from flask import Flask

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/")
def index():
    # choose a movie by invoking our new function
    movie = get_random_movie()
    tomorrow_movie = get_random_movie()

    # build the response string
    content = "<h1>Movie of the Day</h1>"
    content += "<ul>"
    content += "<li>" + movie + "</li>"
    content += "</ul>"

    # TODO: pick another random movie, and display it under
    content += "<h1>Tommorrow's Movie</h1>"
    content += "<ul>"
    content += "<li>" + tomorrow_movie + "</li>"
    content += "</ul>"

    return content

def get_random_movie():
    # TODO: make a list with at least 5 movie titles
    movies = ["The Big Lebowski", "Ghost in the Shell", "Pacific Rim", "Lord of the Rings - Fellowship of the Ring", "Moana"]
    # TODO: randomly choose one of the movies, and return it
    return random.choice(movies)


app.run()
