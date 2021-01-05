import argparse
from wallauto.wallpaper import WallpaperClient


def wallCommands():
    wallpaper_cmd = argparse.ArgumentParser(
        prog='wallpaper',
        description=('sets image requested from some Subreddit as wallpaper.')
    )
    # wallpaper_cmd.add_argument(
    #     'Wallpaper',
    #     metavar='wallpaper',
    #     help='sets a wallpaper.'
    # )
    cmd_group = wallpaper_cmd.add_mutually_exclusive_group(required=True)
    cmd_group.add_argument(
        '-r',
        '--random',
        action='store_true',
        help=('get a random image from Subreddits and sets it as a wallpaper.')
    )
    cmd_group.add_argument(
        '-rd',
        '--rand_depot',
        action='store_true',
    )
    wallpaper_args = wallpaper_cmd.parse_args()

    wallpaper = WallpaperClient()
    img = None
    if wallpaper_args.random:
        img = wallpaper.wallpaper_random()
    elif wallpaper_args.rand_depot:
        img = wallpaper.wallpaper_random_from_depot()
    for key, value in sorted(img.items()):
        print('\t', key, ':', value)


if __name__ == "__main__":
    wallCommands()
