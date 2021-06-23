""" Class for handle Pexels API. """

import re

import requests


class PexelsConstructor:
    """ Handle communication with Pexels. """

    _base_url = 'https://api.pexels.com/v1'

    _api_key = None

    _end_point = 'curated'
    _end_points_data = {
        'curated': {
            'name': 'curated',
            'parameters': ['page', 'per_page']
        },
        'search': {
            'name': 'search',
            'parameters': [
                'query',
                'orientation',
                'size',
                'color',
                'locale',
                'page',
                'per_page',
            ]
        }
    }

    _url = None

    def __init__(self):
        self._query = 'mountain'
        self._orientation = 'landscape'
        self._size = None
        self._color = None
        self._locale = None
        self._page = None
        self._per_page = 15

    # Setters and Getters.
    # ------------------------------------------------------------

    @property
    def api_key(self):
        """ api_key getter. """

        return self._api_key

    @api_key.setter
    def api_key(self, value):
        self._api_key = value

    @property
    def end_point(self):
        """ end_point getter. """

        return self._end_point

    @end_point.setter
    def end_point(self, value):
        """ Accepts to options: search and curated. """

        valid_options = ['search', 'curated']

        if value in valid_options:
            self._end_point = value
        else:
            raise Exception(
                f'Values allowed for end_point: {", ".join(valid_options)}'
            )

    @property
    def query(self):
        """ query getter. """

        return self._query

    @query.setter
    def query(self, value):
        if value is not None:
            self._query = value

    @property
    def orientation(self):
        """ orientation getter. """

        return self._orientation

    @orientation.setter
    def orientation(self, value):
        """ Valid options: landscape, portrait or square """

        if value is not None:
            valid_options = ['landscape', 'portrait', 'square']

            if value in valid_options:
                self._orientation = value
            else:
                raise Exception(
                    f'Values allowed for orientation: {", ".join(valid_options)}'
                )

    @property
    def size(self):
        """ size getter. """

        return self._size

    @size.setter
    def size(self, value):
        if value is not None:
            valid_options = ['large', 'medium', 'small']

            if value in valid_options:
                self._size = value
            else:
                raise Exception(
                    f'Values allowed for size: {", ".join(valid_options)}'
                )

    @property
    def color(self):
        """ color getter. """

        return self._color

    @color.setter
    def color(self, value):
        if value is not None:
            valid_options = ['red', 'orange', 'yellow',
                            'green', 'turquoise','blue',
                            'violet','pink','brown',
                            'black','gray','white']

            color_hex = re.search(r'#[a-zA-Z\d]{6}', value)


            if value in valid_options or color_hex:
                self._color = value
            else:
                raise Exception(
                    f'Values allowed are hexidecimal or: {", ".join(valid_options)}'
                )

    @property
    def locale(self):
        """ locale getter. """

        return self.locale

    @locale.setter
    def locale(self, value):
        if value is not None:
            valid_options = ['en-US', 'pt-BR', 'es-ES', 'ca-ES', 'de-DE',
                             'it-IT', 'fr-FR', 'sv-SE', 'id-ID', 'pl-PL',
                             'ja-JP', 'zh-TW', 'zh-CN', 'ko-KR', 'th-TH',
                             'nl-NL', 'hu-HU', 'vi-VN', 'cs-CZ', 'da-DK',
                             'fi-FI', 'uk-UA', 'el-GR', 'ro-RO', 'nb-NO',
                             'sk-SK', 'tr-TR', 'ru-RU']

            if value in valid_options:
                self._locale = value
            else:
                raise Exception(
                    f'Values allowed for locale: {", ".join(valid_options)}'
                )

    @property
    def per_page(self):
        """ per_page getter. """

        return self._per_page

    @per_page.setter
    def per_page(self, value):
        if value is not None:
            if not isinstance(value, int):
                raise Exception('per_page: Only integers are allowed.')

            if value > 80 or value < 15:
                raise Exception('per_page: Value minimum: 15. Value maximum: 80.')

            self._per_page = value

    # Methods.
    # ------------------------------------------------------------

    def get_url(self):
        """ Get URL build. """

        return self._url

    def _url_builder(self):
        """ Creates a URL """
        end_point = self._end_points_data[self._end_point]
        url = f'{self._base_url[:]}/{end_point["name"]}'
        attrs = vars(self)
        parameters = ''

        for parameter in end_point['parameters']:
            key = '_' + parameter

            if attrs[key] is not None:
                parameters += f'&{parameter}={attrs[key]}'

        if parameters:
            url += f'?{parameters[1:]}'

        self._url = url

        return url

    def request(self):
        """ Make request to curated end point. """

        if not self._api_key:
            raise Exception('No API key.')

        url = self._url_builder()

        headers = { 'Authorization': self._api_key }
        response = requests.get(url, headers=headers)

        return response.json()


class PexelsClient:
    """ Client class. """

    @staticmethod
    def curated(api_key, **params):
        """ Get curated images. """
        pexels = PexelsConstructor()
        pexels.end_point = 'curated'
        pexels.api_key = api_key
        pexels.page = params.get('page', None)
        pexels.per_page = params.get('per_page', 15)
        response = pexels.request()

        return [photo for photo in response['photos']
                if photo['width'] > photo['height']]

    @staticmethod
    def search(api_key, **params):
        """ Get images by search. """

        pexels = PexelsConstructor()
        pexels.api_key = api_key
        pexels.end_point = 'search'
        pexels.query = params.get('query', 'mountain')
        pexels.orientation = params.get('orientation', 'landscape')
        pexels.size = params.get('size', 'medium')
        pexels.color = params.get('color', None)
        pexels.locale = params.get('locale', None)
        pexels.per_page = params.get('per_page', None)

        return pexels.request()['photos']
