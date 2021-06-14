import pathlib

default_directory = pathlib.Path.home() / '.config/wallauto/'

default_file_name = 'settings.yml'

schema = {
    'database': {
        'path': str(default_directory / 'image_storage.database'),
        'name': 'image_storage.database',
    },
    'image_storage': str(default_directory / 'image_storage'),
    'secret': {
        'provider': 'pexels',
        'api_key': '',
    },
    'remove_on_change': True,
}

# Pexels
# ------------------------------------------------------------
pexels_api = {
    'base_url': 'https://api.pexels.com/v1/'
}
