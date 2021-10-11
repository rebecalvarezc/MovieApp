CREATE_MOVIE_TABLE = """ CREATE TABLE IF NOT EXISTS movies (
    movie_id  INTEGER NOT NULL UNIQUE,
    title TEXT NOT NULL,
    release_timestamp REAL NOT NULL,
    PRIMARY KEY(movie_id AUTOINCREMENT)
);"""

CREATE_USER_TABLE = """ CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER NOT NULL UNIQUE,
    name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    username TEXT NOT NULL UNIQUE,
    PRIMARY KEY (user_id AUTOINCREMENT)
);"""

CREATE_WATCHED_TABLE = """ CREATE TABLE IF NOT EXISTS watched_movies (
    user_id INTEGER NOT NULL,
    movie_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id), 
    FOREIGN KEY (movie_id) REFERENCES movies(movie_id)
);"""

CHECK_MOVIE = "SELECT title, release_timestamp FROM movies WHERE title = ? AND release_timestamp = ? LIMIT 1;"

INSERT_MOVIE = "INSERT INTO movies (title, release_timestamp) VALUES (?, ?);"

SHOW_MOVIES = "SELECT movie_id, title, release_timestamp FROM movies;"

UPCOMING_MOVIES = "SELECT movie_id, title, release_timestamp FROM movies WHERE release_timestamp > ?;"

USERS_IDS = "SELECT user_id FROM users WHERE username = ? LIMIT 1;"

MOVIES_IDS = "SELECT title FROM movies WHERE movie_id = ? LIMIT 1;"

ADD_WATCHED_MOVIE = "INSERT INTO  watched_movies (user_id, movie_id) VALUES (?, ?);"

ADD_USER = "INSERT INTO users(name, last_name, username) VALUES (?,?,?);"

VIEW_WATCHED_MOVIES = """SELECT movies.* 
    FROM movies 
        JOIN watched_movies 
        ON movies.movie_id = watched_movies.movie_id 
        JOIN users
        ON users.user_id = watched_movies.user_id
        WHERE users.username = ?;"""

SEARCH_MOVIE = """SELECT * FROM movies WHERE title LIKE ?;"""
