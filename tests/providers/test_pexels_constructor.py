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

    def test_curated_response(self):
        """ Test curated response. """
        pexels = PexelsConstructor()
        pexels.api_key = self.api_key
        pexels.query = 'curated'
        pexels.per_page = 30

        response = pexels.request()

        self.assertEqual(30, response['per_page'])
        self.assertEqual(len(response['photos']), 30)

    def test_search_response(self):
        """ Test search response. """
        pexels = PexelsConstructor()
        pexels.api_key = self.api_key
        pexels.end_point = 'search'
        pexels.query = 'forest'
        pexels.orientation = 'landscape'
        pexels.size = 'medium'
        pexels.color = 'blue'
        pexels.locale = 'es-ES'
        pexels.per_page = 40

        response = pexels.request()

        self.assertEqual(40, response['per_page'])
        self.assertEqual(len(response['photos']), 40)
