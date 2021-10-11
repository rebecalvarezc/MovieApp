from datetime import datetime
import sqlite3
from database_queries import *

connection = sqlite3.connect('movie_database.db')


def create_database():
    """
    This function creates the database if it does not exists.
    """
    with connection:
        connection.execute(CREATE_MOVIE_TABLE)
        connection.execute(CREATE_USER_TABLE)
        connection.execute(CREATE_WATCHED_TABLE)


def add_movies(movie_name: str, release_date: float) -> bool:
    """
    This function adds a movie to the database.

    :param movie_name: movie name
    :param release_date: movie release date
    :return: bool
    """
    with connection:
        movie_exists = connection.execute(CHECK_MOVIE, (movie_name, release_date)).fetchone()
        if movie_exists is None:
            connection.execute(INSERT_MOVIE, (movie_name, release_date))
            return True
        return False


def get_movies(upcoming: bool = False) -> list[tuple]:
    """
    This function shows movie data depending on the given value.

    :param upcoming: True for upcoming movies, False for all movies
    :return: list[tuple]
    """
    with connection:
        movies = connection.cursor()
        if not upcoming:
            return movies.execute(SHOW_MOVIES).fetchall()

        now = datetime.now().timestamp()
        upcoming_list = movies.execute(UPCOMING_MOVIES, (now,)).fetchall()
        if upcoming_list is not None:
            return upcoming_list
        return []


def new_watched_movie(username: str, movie_id: int) -> bool:
    """
    This function changes the timestamp of a movie that's been already watched by the user.

    :param movie_id: movie ID
    :param username: user name
    :return: bool
    """
    with connection:
        all_movies = connection.execute(MOVIES_IDS, (movie_id,)).fetchone()
        all_usernames = connection.execute(USERS_IDS, (username,)).fetchone()
        if all_usernames is not None and all_movies is not None:
            connection.execute(ADD_WATCHED_MOVIE, (all_usernames[0], movie_id))
            return True
        return False


def add_user(name: str, last_name: str, username: str) -> None:
    """
    This function adds a user into the database.
    :param1 name: user name
    :param2 last_name: user last name
    :param3 username: user username
    """
    with connection:
        connection.execute(ADD_USER, (name, last_name, username))


def view_watched_movies(username: str) -> list[tuple]:
    """
    This function gets all movies marked as watched in the database.

    :param1 username: user username
    :return: list[tuple]
    """
    with connection:
        return connection.execute(VIEW_WATCHED_MOVIES, (username,)).fetchall()


def search_movies(title: str) -> list[tuple]:
    """
    This function allows to user to search a movie that contains on its title the information the user provides.
    :param1 title: movie title
    """
    with connection:
        search = '%' + title + '%'
        return list(connection.execute(SEARCH_MOVIE, (search,)))
