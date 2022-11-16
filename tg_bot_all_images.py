import argparse
import os
import random
import time
from os import listdir
from os.path import isfile
from os.path import join as joinpath
from tkinter import BOTH

import requests
import schedule
import telegram
from dotenv import load_dotenv

import image_files_listdir

def upload_images_to_tg(Path, bot, chat_id):
    Path = 'nasa' + '/'
    path_files = image_files_listdir.files_listdir(Path)
    bot.send_document(chat_id=chat_id, document=open(f"{Path} + {path_files}", 'rb'))


def shedule():
    schedule.every().hour.do(upload_images_to_tg)

   
if __name__ == '__main__':
    load_dotenv()

    parser = argparse.ArgumentParser()
    parser.add_argument("Path")
    args = parser.parse_args()
    Path = args.Path
    Path = Path + '/'

    bot_token = os.getenv('TG_BOT_TOKEN')
    chat_id = os.getenv('TG_CHAT_ID')
    hours_break = os.getenv('TG_SEND_HOURS_BREAK')

    bot = telegram.Bot(token=bot_token)
    bot.token = bot._validate_token(bot_token)

    while True:
        upload_images_to_tg(Path, bot, chat_id)
        schedule.run_pending()
        time.sleep(int(hours_break)*60*60)
