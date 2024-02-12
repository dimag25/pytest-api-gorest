import base64

from Consts import API_BASE_URL, TOKEN


class api:
    def __init__(self, endpoint):
        # for docker need to use : host.docker.internal , for your local machine : localhost.
        self.api_endpoint = f'{API_BASE_URL}/{endpoint}'
        self.authorization = f'Bearer {TOKEN}'
