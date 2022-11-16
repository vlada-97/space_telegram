import os
import pathlib
import requests
from datetime import datetime 
from dotenv import load_dotenv
import download_image


def fetch_nasa_epic(folder_name, api_key):

    link_epic = "https://api.nasa.gov/EPIC/api/natural/image"
    params = {
        "api_key": api_key
    }

    response = requests.get(link_epic, params = params)    
    response.raise_for_status()
  
    epic_images = response.json()
    for image in epic_images:
        filename = image["image"]
        epic_image_date = image["date"]
        epic_image_date = datetime.fromisoformat(epic_image_date).strftime("%Y/%m/%d")
        link_path = f"https://api.nasa.gov/EPIC/archive/natural/{epic_image_date}/png/{filename}.png"
        file_path = f"{folder_name}/{filename}.png"
        download_image.get_image(link_path, file_path, params)


if __name__ == '__main__':
    load_dotenv()
    api_key = os.getenv('NASA_API_KEY')
    folder_epic = os.getenv("FOLDER_EPIC")
    pathlib.Path(folder_epic).mkdir(parents=True, exist_ok=True)
    fetch_nasa_epic(folder_epic, api_key)
