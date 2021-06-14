import argparse
from wallauto.wallpaper import WallpaperClient


# Initial configuration
# ------------------------------------------------------------
def config():
    config = argparse.ArgumentParser(
        prog='conf',
        description=('Creates a program configurations.'))
    config.add_argument(
        'Init',
        metavar='init',
        help='Set configurations.'
    )
    config.add_argument(
        '-f',
        '--force',
        action='store_true',
        help=('Force regenerate essentials configurations and files. '
              'Be careful!')
    )
    config_args = config.parse_args()
    if config_args.Init:
        confirm = False
        if config_args.force:
            confirm = input('WARNING: This process can remove your'
                            ' custom configurations. Do you want'
                            'continue? y/n: ')
            confirm = True if confirm == 'y' else False
        WallpaperClient.init_conf(force=confirm)
    else:
        print('Select an argument.')


if __name__ == "__main__":
    config()
