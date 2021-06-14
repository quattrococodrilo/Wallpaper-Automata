import pathlib

default_directory = pathlib.Path.home() / '.config/wallauto/'

default_file_name = 'settings.yml'

schema = {
    'image_database': str(default_directory / 'image_db.database'),
    'image_storage': str(default_directory / 'image_storage'),
    'remove_on_change': True,
    'secret': {
        'provider': 'pexels',
        'api_key': '',
    },
}

# Pexels
# ------------------------------------------------------------
pexels_api = {
    'base_url': 'https://api.pexels.com/v1/'
}
