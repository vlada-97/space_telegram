import os
import argparse
import requests
import pathlib
from dotenv import load_dotenv

import download_image


def fetch_spacex_your_launch(folder_name, id_spacex):

    url_spacex = f"https://api.spacexdata.com/v5/launches/{id_spacex}"
    response = requests.get(url_spacex)
    response.raise_for_status()
    if response.ok:
        photos_spacex = [url_spacex for url_spacex in response.json()['links']['flickr']['original']]
          
    for number, link in enumerate(photos_spacex):
        file_path = f"{folder_name}/spacex{number}.jpg"
        download_image.get_image(link, file_path)


def fetch_spacex_last_launch(folder_name):
    url_spacex = "https://api.spacexdata.com/v5/launches/"
    response = requests.get(url_spacex)
    response.raise_for_status()

    launches = response.json()
    for launch in launches:
        if launch["links"]["flickr_images"]:
            photos_spacex = launch["links"]["flickr_images"]
            break
          
    for number, link in enumerate(photos_spacex):
        file_path = f"{folder_name}/spacex{number}.jpg"
        download_image.get_image(link, file_path)


if __name__ == "__main__":
    load_dotenv()
    parser = argparse.ArgumentParser()
    parser.add_argument("id_spacex")
    args = parser.parse_args()
    id_spacex = args.id_spacex

    folder_spacex = os.getenv("FOLDER_SPACEX")
    pathlib.Path(folder_spacex).mkdir(parents=True, exist_ok=True)

    try:
        fetch_spacex_your_launch(folder_spacex, str(id_spacex))
    except requests.exceptions.HTTPError as error:
        print("Can't get data from server:\n{0}.\nDownloading the last launch.".format(error))
        fetch_spacex_last_launch(folder_spacex)
