import argparse

from wallauto.wall_configs import WallConfigs


# Initial configuration
# ------------------------------------------------------------
def config_commands():
    wall_conf = WallConfigs()

    config = argparse.ArgumentParser(
        prog='conf',
        description=('Creates a program configurations.')
    )

    config.add_argument(
        'init',
        metavar='init',
        help='Set start configurations.'
    )

    config_args = config.parse_args()

    if config_args.init:
        wall_conf.create_settings()\
            .load_custom_user_settings()\
            .create_image_storage()


if __name__ == "__main__":
    config_commands()
