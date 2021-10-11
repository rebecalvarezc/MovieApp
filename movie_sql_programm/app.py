from datetime import datetime
from pprint import pprint
import os
import global_functions as gf

MAIN_MENU = """\nWelcome to the watchlist app!
Please select one of the following options:

1.- Add a new movie.
2.- View upcoming movies.
3.- View all movies.
4.- Add watched movies.
5.- View watched movies.
6.- Add user to the app.
7.- Search a movie by title.
8.- Exit.

Your selection: """


def add_function():
    movie_name = input('Movie name: ').title()
    date = input('Release date (dd-mm-yyyy): ')
    release_date = datetime.strptime(date, '%d-%m-%Y').timestamp()
    added = gf.add_movies(movie_name, release_date)
    if added:
        print('Movie successfully added :)\n')
    else:
        print('The movie is already saved in our database.')


def print_movies(movies: list):
    for movie_id, title, release_timestamp in movies:
        release_date = datetime.fromtimestamp(release_timestamp)
        pprint(f'{movie_id}: {title} (on {release_date.strftime("%b %d %Y")})')


def show_upcoming_movies():
    any_upcoming_movie = gf.get_movies(True)
    if not any_upcoming_movie:
        print('There aren\'t any upcoming movies.')
    else:
        print('-- Upcoming movies --')
        print_movies(any_upcoming_movie)
        print('-----')


def add_watched_movie():
    while True:
        print_movies(gf.get_movies())
        try:
            user = input('Username: ')
            movie_id = int(input('Movie ID: '))
            movie_watched = gf.new_watched_movie(user, movie_id)
            if movie_watched:
                print('Movie added to the list :)')
            else:
                print('Movie ID/Username not found.')
            break
        except ValueError:
            print('Introduce a number in "Movie ID".')
            continue


def user_interface():
    while (user_selection := int(input(MAIN_MENU))) != 8:
        os.system('cls')
        gf.create_database()
        if user_selection == 1:
            add_function()

        elif user_selection == 2:
            show_upcoming_movies()

        elif user_selection == 3:
            print('-- All movies --')
            movies = gf.get_movies()
            print_movies(movies)
            print('------')

        elif user_selection == 4:
            add_watched_movie()

        elif user_selection == 5:
            username = input('Username: ')
            watched_movies = gf.view_watched_movies(username)
            if not watched_movies:
                print('There are no watched movies on your list.')
            else:
                print('\n-- Watched movies --')
                print_movies(watched_movies)
        elif user_selection == 6:
            name = input('Introduce your name: ').title()
            last_name = input('Introduce your last name: ').title()
            user_name = input('Introduce your username: ').lower()
            gf.add_user(name, last_name, user_name)
            print('User added successfully!')

        elif user_selection == 7:
            title = input('Introduce the movie title: ').title()
            found_movie = gf.search_movies(title)
            if found_movie:
                print_movies(found_movie)
            else:
                print('Movie not found.')

        else:
            print('Introduce a valid option.')
    print('Goodbye :)')


if __name__ == '__main__':
    user_interface()
