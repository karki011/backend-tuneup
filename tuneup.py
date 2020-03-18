#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "???"
import io
import cProfile
import pstats
import functools
import timeit


def profile(func):
    """A function that can be used as a decorator to measure performance"""
    # You need to understand how decorators are constructed and used.
    # Be sure to review the lesson material on decorators, they are used
    # extensively in Django and Flask.
    # raise NotImplementedError("Complete this decorator function")
    @functools.wraps(func)
    def inner_function(*args, **kwargs):

        pro_object = cProfile.Profile()
        pro_object.enable()
        result = func(*args, **kwargs)
        pro_object.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pro_object, stream=s).strip_dirs().sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())

        return result
    return inner_function


def read_movies(src):
    """Returns a list of movie titles"""
    print('Reading file: {}'.format(src))
    with open(src, 'r') as f:
        return f.read().splitlines()


def is_duplicate(title, movies):
    """returns True if title is within movies list"""
    for movie in movies:
        if movie.lower() == title.lower():
            return True
    return False


@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list"""
    movies = read_movies(src)
    movies.sort()
    # duplicates = []
    # while movies:
    #     movie = movies.pop()
    #     if movie in movies:
    #         duplicates.append(movie)
    duplicates = [m1 for m1, m2 in zip(movies[1:], movies[:-1]) if m1 == m2]
    print(duplicates)
    return duplicates


def timeit_helper():
    """Part A:  Obtain some profiling measurements using timeit"""
    # YOUR CODE GOES HERE
    t = timeit.Timer(functools.partial(find_duplicate_movies, 'movies.txt'))
    time_result = min(t.repeat(repeat=7, number=5))/5
    print("Best time across 7 repeats of 5 runs per repeat:",
          time_result, " seconds")


def main():
    """Computes a list of duplicate movie entries"""
    result = find_duplicate_movies('movies.txt')
    print('Found {} duplicate movies:'.format(len(result)))
    print('\n'.join(result))


if __name__ == '__main__':
    main()
