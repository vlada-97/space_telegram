import os
import requests
import pathlib
from urllib.parse import urlparse
from dotenv import load_dotenv

import download_image


def get_extension(url):
    url_parse = urlparse(url)
    url_path = url_parse.path
    
    return os.path.splitext(url_path)[1]

def fetch_nasa(folder_name, api_key):

    url_apod = "https://api.nasa.gov/planetary/apod"

    count = 30
    params = {
        "api_key": api_key,
        'media_type': 'image',
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
            download_image.get_image(nasa_link_image, file_path, params)


if __name__ == '__main__':
    load_dotenv()

    folder_nasa = os.getenv('FOLDER_NASA')
    api_key = os.getenv('NASA_API_KEY')
    
    pathlib.Path(folder_nasa).mkdir(parents=True, exist_ok=True)
    fetch_nasa(folder_nasa, api_key)
