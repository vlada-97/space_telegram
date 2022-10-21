import os
import requests
import pathlib
from urllib.parse import urlparse


def get_image(url, way, params = None):
    response = requests.get(url, params = params)
    response.raise_for_status()

    with open(way, 'wb') as file:
        file.write(response.content)


def get_extension(url):
    url_parse = urlparse(url)
    url_path = url_parse.path
    
    return os.path.splitext(url_path)[1]

def fetch_nasa(folder_name, api_key):

    url_apod = "https://api.nasa.gov/planetary/apod"

    count = 30
    params = {
        "api_key": api_key,
        "count": count
    }

    response = requests.get(url_apod, params=params)
    response.raise_for_status()

    nasa_images = response.json()

    for number ,image_nasa in enumerate(nasa_images):
        if image_nasa["url"]:
            nasa_link_image = image_nasa["url"]
            extension = get_extension(nasa_link_image)
            file_path = f"{folder_name}/nasa{number}{extension}"
            get_image(nasa_link_image, file_path, params)


def main():
    folder_nasa = os.environ["FOLDER_NASA"]
    api_key = os.environ['API_KEY']
    
    pathlib.Path(folder_nasa).mkdir(parents=True, exist_ok=True)
    fetch_nasa(folder_nasa, api_key)