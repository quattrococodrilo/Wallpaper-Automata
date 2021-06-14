import argparse
from wallauto.yamlmanager import YamlManger
from wallauto.wallpaper import WallpaperClient


# Modify configuration file options
# ------------------------------------------------------------
def modify():
    wallpaper = WallpaperClient()
    config_file = wallpaper.get_config_file()
    config_db = YamlManger(config_file)
    config_data = config_db.get()
    # Arguments
    # --------------------------------------------------------
    modify_option = argparse.ArgumentParser(
        prog='Modifier',
        description=('set a value to configuration file option.')
    )
    # modify_option.add_argument(
    #     'Modify',
    #     metavar='modify',
    #     help=('modify configuration file options.')
    # )
    modify_option.add_argument(
        '-ap',
        '--amount_post',
        action='store',
        type=int,
        default=config_data['amount_post'],
        help=('amount of post to retrieve.'),
    )
    modify_option.add_argument(
        '-don',
        '--delete_on_change',
        action='store_true',
        default=config_data['delete_on_change'],
        help=('delete previous image used as wallpaper.')
    )
    modify_option.add_argument(
        '-f',
        '--filter',
        action='store',
        type=str,
        choices=['top', 'hot', 'new', 'rising'],
        default=config_data['filter'],
        help=('select filer one filter: top, hot, new, rising'),
    )
    modify_option.add_argument(
        '-imgdb',
        '--image_db',
        action='store',
        type=str,
        default=config_data['image_db'],
        help=('file to save image info.')
    )
    modify_option.add_argument(
        '-imgd',
        '--image_depot',
        action='store',
        type=str,
        default=config_data['image_depot'],
        help=('directory where the images will save.')
    )
    modify_option.add_argument(
        '-sra',
        '--show_reddit_account',
        action='store_true',
        help=('show account info.')
    )
    modify_option.add_argument(
        '-ci',
        '--client_id',
        action='store',
        type=str,
        default=config_data['reddit_account']['client_id'],
        help=('change client id')
    )
    modify_option.add_argument(
        '-cs',
        '--client_secret',
        action='store',
        type=str,
        default=config_data['reddit_account']['client_secret'],
        help=('change client secret')
    )
    modify_option.add_argument(
        '-ua',
        '--user_agent',
        action='store',
        type=str,
        default=config_data['reddit_account']['user_agent'],
        help=('change user_agent')
    )
    modify_option.add_argument(
        '-ssub',
        '--show_subreddits',
        action='store_true',
        help='shows Subreddits list.'
    )
    modify_option.add_argument(
        '-asub',
        '--add_subreddit',
        action='store',
        nargs='*',
        help=('add a Subreddit to list.')
    )
    modify_option.add_argument(
        '-rsub',
        '--rm_subreddit',
        action='store',
        type=int,
        help=('remove Subreddit from list by its index.')
    )
    modify_option.add_argument(
        '-tf',
        '--time_filter',
        action='store',
        type=str,
        choices=['all', 'day', 'hour', 'month', 'week', 'year'],
        default=config_data['time_filter'],
        help=('time to filter post, select one of these: '
              'all, day, hour, month, week, year')
    )

    # Save value options
    # --------------------------------------------------------
    modify_args = modify_option.parse_args()
    config_data['amount_post'] = modify_args.amount_post
    config_data['delete_on_change'] = modify_args.delete_on_change
    config_data['filter'] = modify_args.filter
    config_data['image_db'] = modify_args.image_db
    config_data['image_depot'] = modify_args.image_depot
    config_data['reddit_account']['client_id'] = modify_args.client_id
    config_data['reddit_account']['client_secret'] = modify_args.client_secret
    config_data['reddit_account']['user_agent'] = modify_args.user_agent
    config_data['time_filter'] = modify_args.time_filter
    if modify_args.show_reddit_account:
        reddit_account = config_data['reddit_account'].items()
        for key, value in reddit_account:
            print(f'\t{key}: {value}')
    if modify_args.show_subreddits:
        subreddits = config_data['subreddits']
        for index, item in enumerate(subreddits):
            print(f'\t{index + 1}. {item}')
    if modify_args.add_subreddit:
        config_data['subreddits'] = [
            *config_data['subreddits'],
            *modify_args.add_subreddit
        ]
    if modify_args.rm_subreddit:
        del config_data['subreddits'][modify_args.rm_subreddit - 1]
    config_db.set(config_data)
    for k, v in config_data.items():
        if type(v) == dict:
            print('\t', k, ':')
            for key, value in v.items():
                print('\t\t', key, ':', value)
        elif type(v) == list:
            print('\t', k, ':')
            for value in v:
                print('\t\t', '-', value)
        else:
            print('\t', k, ':', v)


if __name__ == "__main__":
    modify()
