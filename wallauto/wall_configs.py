""" Module for configurations. """

import pathlib

import wallauto.settings as settings
from wallauto.yamlmanager import YamlManger


class WallConfigs:
    """ Handles configurations. """

    var = None

    def _create_settings(self):
        """ Creates a directory for settings if not exists. """

        settings_dir = pathlib.Path(settings.default_directory)
        settings_file = settings_dir / settings.default_file_name

        if not settings_dir.parent.exists():
            raise Exception(f'{settings_dir.parent} not exists.')

        if not settings_dir.exists():
            settings_file.mkdir()

        if not settings_file.exists():
            yml = YamlManger(settings_file)
            yml.set(settings.schema)

    def _create_image_storage(self):
        """Creates image storage."""
