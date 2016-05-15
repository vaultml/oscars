import pandas as pd


class award(object):
    best_actor = 0
    support_actor = 1
    best_actress = 2
    support_actress = 3
    best_picture = 4
    directing = 5
    acting = [best_actor, support_actor, best_actress, support_actress, best_picture, directing]
    all = [best_actor, support_actor, best_actress, support_actress, best_picture, directing]

    def __init_(self):
        pass


def read_movies():
    movies = pd.read_csv('movies.csv', dtype={'imdbid': str}, index_col=None)
    return movies


def read_talents():
    return pd.read_csv('talents.csv', dtype={'talentid': str}, index_col=None, parse_dates=['birth_date'])


def read_awards():
    return pd.read_csv('awards.csv', dtype={'imdbid': str, 'talentid': str}, index_col=None)


def read_roles():
    return pd.read_csv('roles.csv', dtype={'imdbid': str, 'talentid': str}, index_col=None)
