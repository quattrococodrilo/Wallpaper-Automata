""" Class for handle Pexels API. """

import requests


class PexelsConstructor:
    """ Handle communication with Pexels. """

    _base_url = 'https://api.pexels.com/v1/'

    _api_key = None

    _end_point = 'curated'

    _query = 'mountain'
    _orientation = 'landscape'
    _size = None
    _color = None
    _locale = None
    _page = None
    _per_page = 15

    # Setters and Getters.
    # ------------------------------------------------------------

    @property
    def api_key(self):
        return self._api_key

    @api_key.setter
    def api_key(self, value):
        self._api_key = value

    @property
    def end_point(self):
        return self._end_point

    @end_point.setter
    def end_point(self, value):
        """ Accepts to options: search and curated. """

        valid_options = ['search', 'curated']

        if value in valid_options:
            self._end_point = value
        else:
            raise Exception(f'Values allowed: {", ".join(valid_options)}')

    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value):
        self._query = value

    @property
    def orientation(self):
        return self._orientation

    @orientation.setter
    def orientation(self, value):
        """ Valid options: landscape, portrait or square """

        valid_options = ['landscape', 'portrait', 'square']

        if value in valid_options:
            self._orientation = value
        else:
            raise Exception(f'Values allowed: {", ".join(valid_options)}')

    @property
    def per_page(self):
        return self._per_page

    @per_page.setter
    def per_page(self, value):
        if type(value) == int and value <= 80:
            self._per_page = value
        else:
            raise Exception(f'Only integers are allowed, maximum: 80')

    # URL methods.
    # ------------------------------------------------------------

    def _url_builder_curated(self):
        """ Creates a curated URL. """
        url = f'{self._base_url[:]}/{self._query}'

        if self._per_page:
            url += f'?per_page={self._per_page}'

        return url

    def _url_builder_search(self):
        pass


    def _request_curated(self):
        """ Make request to curated end point. """

        if not self._api_key:
            raise Exception('No API key.')

        url = self._url_builder_curated()

        headers = { 'Authorization': self._api_key }
        response = requests.get(url, headers=headers)

        return response.json()



    def _request_search(self):
        pass

    def request(self):
        if self._end_point == 'curated':
            return self._request_curated()

        if self._end_point == 'search':
            return self._request_search()
