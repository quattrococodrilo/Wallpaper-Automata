""" Tests for RedditClient module. """

import pathlib
from wallauto.reddit import RedditClient
from wallauto.yamlmanager import YamlManger


def secret_reddit():
    return YamlManger(
        pathlib.Path.cwd() / 'data' / 'secrets.yml'
    ).get()


def test_get_top_posts_from_reddit():
    secret = secret_reddit()
    reddit = RedditClient(
        **secret
    )
    posts = reddit.sub()
    assert len(posts) == 25


def test_get_hot_post_of_day():
    limit = 15
    secret = secret_reddit()
    reddit = RedditClient(
        **secret
    )
    posts = reddit.sub(limit=limit, secc='hot', time_filter='day')
    assert len(posts) == limit and 'http' in posts[0].url


def test_get_rising_post():
    limit = 15
    secret = secret_reddit()
    reddit = RedditClient(
        **secret
    )
    posts = reddit.sub(limit=limit, secc='rising')
    assert len(posts) == limit and 'http' in posts[0].url


def test_get_new_post():
    limit = 15
    secret = secret_reddit()
    reddit = RedditClient(
        **secret
    )
    posts = reddit.sub(limit=limit, secc='new')
    assert len(posts) == limit and 'http' in posts[0].url
