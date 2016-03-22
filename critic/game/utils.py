import random
import requests
from bs4 import BeautifulSoup


mn_orig = "Kung Fu Panda 3"                                         # Movie Name
rt_name = mn_orig.replace(" ", "_").lower()                         # Rotten Tomatoes has '_' in between
omdb_name = mn_orig.replace(" ", "+").lower()                       # OMDB wants '+' in between


def get_details():
    """ Open Movie Database API to return specific information """
    raw = requests.get("http://www.omdbapi.com/?t=" + omdb_name + "&r=json")
    # Keys: "Title", "Year", "Released", "Genre", "Director", "Actors", "Plot", "Poster" (300px image)
    movie = raw.json()
    director = movie['Director'].split(",")[0]                      # Director's Full Name
    director_last_name = director.split(" ")[1]                     # Director's Last Name
    actor = movie['Actors'].split(",")[0]                           # Main Actor's Full Name
    actor_fn = actor.split(" ")[0]                                  # Actor First name
    actor_ln = actor.split(" ")[1]                                  # Actor Last Name
    year_filmed = movie['Year']
    poster_img = movie['Poster']

    return director_last_name, year_filmed, actor_fn, actor_ln, poster_img

review_url = "http://www.rottentomatoes.com/m/" + rt_name + "/reviews/?type=top_critics"
r = requests.get(review_url)
soup = BeautifulSoup(r.content, 'html.parser')
reviews = soup.find_all("div", {"class": "the_review"})


def get_reviews():
    """Grabs text for top reviews, filters them, and returns them in a list"""
    random.shuffle(reviews)                                         # Shuffle the reviews
    new_group = []
    d = get_details()
    for item in reviews[0:4]:
        new_group.append(item.text)
    filtered_group = [word.replace(mn_orig, "[Movie]")              # List comprehension to
                          .replace(d[0], "[Director]")                                # filter for the reviews
                          .replace(d[1], "[Date]")                                    # ** consider regex for this **
                          .replace(d[2], "[Actor First Name]")
                          .replace(d[3], "[Actor Name]")
                      for word in new_group]
    return filtered_group

get_reviews()