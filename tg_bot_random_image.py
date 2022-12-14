import argparse
import os
import random
import requests
from os import listdir
from os.path import isfile
from os.path import join as joinpath

import telegram
from dotenv import load_dotenv

import image_files_listdir
PATH = 'nasa' + '/'

def random_photo(bot, chat_id):
    path_files = image_files_listdir.files_listdir(PATH)
    bot.send_document(chat_id=chat_id, document=open(f"{PATH} + {path_files}", 'rb'))


def send_photo(bot, chat_id, img):
    bot.send_document(chat_id=chat_id, document=open(img, 'rb'))
    response = requests.get(img)
    response.raise_for_status()


if __name__ == '__main__':
    load_dotenv()
    parser = argparse.ArgumentParser()
    parser.add_argument("img")
    parser.parse_args()
    args = parser.parse_args()
    img = args.img
    
    bot_token = os.getenv('TG_BOT_TOKEN')
    chat_id = os.getenv('TG_CHAT_ID')
    bot = telegram.Bot(token=bot_token)

    try:
        send_photo(bot, chat_id, img)
    except:
        random_photo(bot, chat_id)
