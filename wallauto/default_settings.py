import pathlib

settings_directory = pathlib.Path.home() / '.confi/wallauto/'

image_storage = pathlib.Path.home() / 'wallauto_storage'

settings_file_name = 'settings.yml'

db_name_sqlite = 'storage.database'

db_name_yml = 'storage.yml'

# Pexels
# ------------------------------------------------------------
pexels_api = {
    'base_url': 'https://api.pexels.com/v1/'
}

