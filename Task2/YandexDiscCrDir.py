import requests


class YaDisc:
    def __init__(self, token_y):
        self.token_y = token_y
        self.headers = {'Content-Type': 'application/json',
                        'Authorization': f'OAuth {self.token_y}'}

    def create_directory(self, test_dir_name):
        create_directory_url = 'https://cloud-api.yandex.net/v1/disk/resources/'
        requests.put(create_directory_url, headers = self.headers,
                     params = {'path': f'/netology_ADPY'})
        response = requests.put(create_directory_url, headers=self.headers,
                                params={'path': f'/netology_ADPY/{test_dir_name}'})
        return response
