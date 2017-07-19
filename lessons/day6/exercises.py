from urllib.request import urlopen
import csv
from time import sleep

def request_google():
    # Try out this function to see what it does
    res = urlopen("http://google.com").read()
    return res

def add_pluses(string):

    # modify a string such that each seperate word is seperated by exactly 1 "+"
    # also lowercase the string
    # make sure there are no trailing spaces in either direction

    # e.g. "Lord    of The Rings" -> "Lord+of+The+Rings"

    return ''

url_base = 'http://www.omdbapi.com/?t={movie_name}&apikey={key}'
api_key = 'ec6483bd'

def movie_api_request(string):

    """

    Plug in the name of a movie, format it by replacing pluses with spaces and make a request
    to the api end point

    """

    return ''

def request_movie_data(list_of_movies):

    """
    Given a list of movies request the data for all these movies

    """

    # don't forget to sleep in between requests
    # otherwise the api will block you

    sleep(3)

    return

def extract_movie_data(list_of_movie_data):

    """
    Given a list of movie data. Extract the name of the movie, the date it was released and all of the scores it recieved

    """

    return

def write_movie_data():

    """
    Use the data 
    """

    # write the data you collected from extract_movie_data to disk as a csv

    return