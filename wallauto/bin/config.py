import argparse

from wallauto.wall_configs import WallConfigs


# Initial configuration
# ------------------------------------------------------------
def config_commands():
    wall_conf = WallConfigs()

    config = argparse.ArgumentParser(
        description=('Creates a program configurations.'),
        epilog='Enjoy and share this program :)',
    )

    config.add_argument(
        'conf',
        metavar='configuration',
        help='creates configuration.'
    )

    config.add_argument(
        '-i',
        '--init',
        action='store_true',
        help='Set start configurations.'
    )

    config.add_argument(
        '-d',
        '--dirs',
        action='store_true',
        help='Create directories.'
    )

    config_args = config.parse_args()

    if config_args.init:
        wall_conf.create_settings()\
            .load_custom_user_settings()\
            .create_image_storage()
        print('Initial configuration was made.')

    if config_args.dirs:
        wall_conf.load_custom_user_settings()\
            .create_image_storage()
        print('Directories created.')

if __name__ == "__main__":
    config_commands()
