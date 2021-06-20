import pathlib
import unittest

import wallauto.settings as settings
from wallauto.providers.pexles import PexelsClient, PexelsConstructor
from wallauto.yamlmanager import YamlManager


class TestPexels(unittest.TestCase):
    """ Test Pexels module """

    api_key = None

    def setUp(self):
        secrets_path = (pathlib.Path(__file__).parent.parent.parent
                        / 'data/secrets.yml')
        yml = YamlManager(secrets_path)
        secrets = yml.get()
        self.api_key = secrets['pexels_api_key']

    # PexelsConstructor
    # ------------------------------------------------------------

    def test_constructor_curated_response(self):
        """ Test curated response. """
        pexels = PexelsConstructor()
        pexels.api_key = self.api_key
        pexels.query = 'curated'
        pexels.per_page = 30

        response = pexels.request()

        self.assertEqual(30, response['per_page'])
        self.assertEqual(len(response['photos']), 30)

    def test_constructor_search_response(self):
        """ Test search response. """
        per_page = 20

        pexels = PexelsConstructor()
        pexels.api_key = self.api_key
        pexels.end_point = 'search'
        pexels.query = 'forest'
        pexels.orientation = 'landscape'
        pexels.size = 'medium'
        pexels.color = 'blue'
        pexels.locale = 'es-ES'
        pexels.per_page = per_page

        response = pexels.request()

        self.assertEqual(len(response['photos']), per_page)
        self.assertEqual(per_page, response['per_page'])

    # PexelsClient
    # ------------------------------------------------------------

    def test_client_curated(self):
        curated = PexelsClient.curated(self.api_key)

        self.assertTrue(len(curated) > 0)

    def test_client_search(self):
        search = PexelsClient.search(self.api_key)

        self.assertTrue(len(search) > 0)
