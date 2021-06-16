import pathlib
import unittest

import wallauto.settings as settings
from wallauto.providers.pexles_constructor import PexelsConstructor
from wallauto.yamlmanager import YamlManager


class TestPexelsConstructor(unittest.TestCase):
    """ Test Pexels module """

    api_key = None

    def setUp(self):
        secrets_path = (pathlib.Path(__file__).parent.parent.parent
                        / 'data/secrets.yml')
        yml = YamlManager(secrets_path)
        secrets = yml.get()
        self.api_key = secrets['pexels_api_key']

    def test_set_query(self):
        """ Test query assignation. """
        pexels = PexelsConstructor()
        pexels.query = 'search'

        self.assertEqual('search', pexels.query)

    def test_curated_response(self):
        """ Test curated response. """
        pexels = PexelsConstructor()
        pexels.api_key = self.api_key
        pexels.query = 'curated'
        pexels.per_page = 30

        response = pexels.request()

        self.assertEqual(30, response['per_page'])
        self.assertEqual(len(response['photos']), 30)
