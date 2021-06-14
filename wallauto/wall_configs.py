""" Module for configurations. """

import pathlib

import wallauto.settings as settings
from wallauto.yamlmanager import YamlManger


class WallConfigs:
    """ Handles configurations. """

    var = None
    settings_dir = None
    settings_file = None

    def __init__(self):
        self.settings_dir = pathlib.Path(settings.default_directory)
        self.settings_file = self.settings_dir / settings.default_file_name

    def create_settings(self):
        """ Creates a directory for settings if not exists. """

        if not self.settings_dir.parent.exists():
            raise Exception(f'{self.settings_dir.parent} not exists.')

        if not self.settings_dir.exists():
            self.settings_file.mkdir()

        if not self.settings_file.exists():
            yml = YamlManger(self.settings_file)
            yml.set(settings.schema)

        return self

    def create_image_storage(self):
        """Creates image storage."""
        image_storage = pathlib.Path(settings.schema['image_storage'])
        image_database = pathlib.Path(settings.schema['image_database'])

        if not image_storage.exists():
            image_storage.mkdir()

        if not image_database.exists():
            image_database.touch()

        return self

    def load_custom_user_settings(self):
        """ Loads custom user settings. """

        return self
