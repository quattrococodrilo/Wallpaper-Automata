import pathlib
import unittest

import wallauto.settings as settings
from wallauto.wall_configs import WallConfigs


class TestConfigMethods(unittest.TestCase):
    """ Test for wallauto configuration. """


    wall_conf = None
    test_dir = pathlib.Path(__file__).parent / '../data/test_area'

    def setUp(self):
        """ Initial configuration. """

        if not self.test_dir.exists():
            self.test_dir.mkdir()

        self.wall_conf = WallConfigs()

    def test_create_settings(self):
        """ Test create settings. """

        settings.default_directory = self.test_dir

        settings_file = self.test_dir / settings.default_file_name

        self.wall_conf._create_settings()

        self.assertTrue(settings_file.exists())

        if settings_file.exists():
            settings_file.unlink()

    def test_create_image_storage(self):
        """Test create image storage."""

        settings.schema['image_storage'] = self.test_dir / 'image_storage'

        database = self.test_dir / 'image_storage.database'

        settings.schema['database']['path'] = self.test_dir

        self.wall_conf._create_image_storage()

        self.assertTrue(settings.schema['image_storage'].exists())

        self.assertTrue(database)

        if settings.schema['image_storage'].exists():
            settings.schema['image_storage'].rmdir()

        if settings.schema['database'].exists():
            settings.schema['database'].unlink()
