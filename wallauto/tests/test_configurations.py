import pathlib
import unittest

import wallauto.settings as settings
from wallauto.wall_configs import WallConfigs
from wallauto.yamlmanager import YamlManger


class TestConfigMethods(unittest.TestCase):
    """ Test for wallauto configuration. """


    wall_conf = None
    test_dir = None
    settings_file = None
    image_storage = None
    image_database = None

    def setUp(self):
        """ Initial configuration. """

        self.test_dir = pathlib.Path(__file__).parent.parent / 'data/test_area'
        self.settings_file = self.test_dir / settings.default_file_name
        settings.default_directory = self.test_dir

        if not self.test_dir.exists():
            self.test_dir.mkdir()

        self.wall_conf = WallConfigs()

    def test_create_settings(self):
        """ Test create settings. """

        self.wall_conf.create_settings()

        self.assertTrue(self.settings_file.exists())

    def test_create_image_storage(self):
        """Test create image storage."""

        self.image_storage = self.test_dir / 'image_storage'
        settings.schema['image_storage'] = self.image_storage

        self.image_database = self.test_dir / 'image_db.database'
        settings.schema['image_database'] = self.image_database

        self.wall_conf.create_image_storage()

        self.assertTrue(settings.schema['image_storage'].exists())

        self.assertTrue(settings.schema['image_database'].exists())

    def test_load_custom_user_settings(self):
        """ Test load custom user settings"""

        yml = YamlManger(self.test_dir / 'test_settings.yml')
        custom_settings = yml.get()

        settings.default_file_name = 'test_settings.yml'

        self.wall_conf.load_custom_user_settings()

        self.assertDictEqual(settings.schema, custom_settings)

    def tearDown(self):
        if self.settings_file.exists():
            self.settings_file.unlink()

        if self.image_storage.exists():
            self.image_storage.rmdir()

        if self.image_database.exists():
            self.image_database.unlink()
