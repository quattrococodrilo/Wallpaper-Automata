from wallauto.reddit import RedditClient
from wallauto.yamlmanager import YamlManger
from pathlib import Path


def get_images():
    secret_file = Path.cwd() / 'data' / 'secrets.yml'
    secrets = YamlManger(secret_file)
    reddit = RedditClient(**secrets.get())
    posts = reddit.sub()
    for post in posts:
        print(post.url)


if __name__ == "__main__":
    get_images()
