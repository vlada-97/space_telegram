import requests


def get_image(url, way, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()

    with open(way, 'wb') as file:
        file.write(response.content)
