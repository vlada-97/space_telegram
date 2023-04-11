import os
import requests
import argparse
import pathlib
from urllib.parse import urlparse
from dotenv import load_dotenv

import download_image


def get_extension(url):
    nasa_url = urlparse(url)
    nasa_extension = nasa_url.path

    return os.path.splitext(nasa_extension)[1]


def fetch_nasa(folder_name, api_key, count):

    apod_url = "https://api.nasa.gov/planetary/apod"

    params = {
        "api_key": api_key,
        "count": count
    }

    response = requests.get(apod_url, params=params)
    response.raise_for_status()

    nasa_images = response.json()

    for number, image_nasa in enumerate(nasa_images):
        if image_nasa['media_type'] == 'image':
            nasa_image_link = image_nasa["url"]
            extension = get_extension(nasa_image_link)
            file_path = os.path.join(folder_name, f'nasa{number}{extension}')
            download_image.get_image(nasa_image_link, file_path, params)


if __name__ == '__main__':
    load_dotenv()
    api_key = os.environ['NASA_API_KEY']

    parser = argparse.ArgumentParser()
    parser.add_argument("--f", default='nasa',
                        help="Folder name to the nasa photo")
    parser.add_argument("--count", default=30,
                        help="Count to the nasa photo downloading")
    args = parser.parse_args()
    nasa_folder = args.f
    count = args.count

    pathlib.Path(nasa_folder).mkdir(parents=True, exist_ok=True)
    fetch_nasa(nasa_folder, api_key, count)
