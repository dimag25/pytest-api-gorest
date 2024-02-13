from Utils.Consts import API_BASE_URL


class api:
    def __init__(self, endpoint):
        self.api_endpoint = f'{API_BASE_URL}/{endpoint}'
