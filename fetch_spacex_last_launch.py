import os
import argparse
import requests
import pathlib

import download_image


def fetch_spacex_launch(folder_name, spacex_id):

    spacex_url = f"https://api.spacexdata.com/v5/launches/{spacex_id}"
    response = requests.get(spacex_url)
    response.raise_for_status()
    spacex_photo_links = [spacex_url for spacex_url in response.json()[
        'links']['flickr']['original']]

    for number, link in enumerate(spacex_photo_links):
        file_path = os.path.join(folder_name, f'spacex{number}.jpg')
        download_image.get_image(link, file_path)


def check_spacex_id_validation(spacex_id):
    spacex_url = f"https://api.spacexdata.com/v5/launches/{spacex_id}"
    response = requests.get(spacex_url)
    return response.ok


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", default='images', help="Photo folder name.")
    parser.add_argument(
        "--spacex_id", default='5eb87d42ffd86e000604b384', help="Spacex id for fetching.")
    args = parser.parse_args()
    spacex_folder = args.path
    spacex_id = args.spacex_id

    try:
        pathlib.Path(spacex_folder).mkdir(parents=True, exist_ok=True)
        fetch_spacex_launch(spacex_folder, str(spacex_id))
    except requests.exceptions.HTTPError as error:
        print(
            "Can't get data from server:\n{0}.\nDownloading the last launch.".format(error))
        if not check_spacex_id_validation(spacex_id):
            fetch_spacex_launch(spacex_folder, spacex_id="latest")
