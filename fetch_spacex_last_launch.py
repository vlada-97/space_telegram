import os
import argparse
import requests
import pathlib
from dotenv import load_dotenv


def get_image(url, way, params = None):
    response = requests.get(url, params = params)
    response.raise_for_status()

    with open(way, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch(folder_name, id):

    url_spacex = "https://api.spacexdata.com/v3/launches/{}".format(id)
    response = requests.get(url_spacex)
    response.raise_for_status()

    launches = response.json()
    for launch in launches:
        if launch["links"]["flickr_images"]:
            photos_spacex = launch["links"]["flickr_images"]
            break
          
    for number, link in enumerate(photos_spacex):
        file_path = f"{folder_name}/spacex{number}.jpg"
        get_image(link, file_path)


def main():
    load_dotenv()
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    args = parser.parse_args()
    url = args.url

    folder_spacex = os.environ["FOLDER_SPACEX"]
    pathlib.Path(folder_spacex).mkdir(parents=True, exist_ok=True)


    try:
        fetch_spacex_last_launch(folder_spacex, str(url))
    except requests.exceptions.HTTPError as error:
        url = "5eb87d42ffd86e000604b384"
        fetch_spacex_last_launch(folder_spacex, str(url))
        print("Can't get data from server:\n{0}".format(error))

if __name__ == "__main__":
    main()