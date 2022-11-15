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


def upload_images_to_tg(Path, bot, chat_id):
    Path = Path + '/'
    for image_file in listdir(Path):
        if isfile(joinpath(Path, image_file)):
            filesindir = os.listdir(Path)
            for files in filesindir:
                random.shuffle(filesindir)
                path_file = os.path.join(files)
                print(path_file)
                bot.send_document(chat_id=chat_id, document=open(Path + path_file, 'rb'))


def shedule():
    schedule.every().hour.do(upload_images_to_tg)

if __name__ == '__main__':
    load_dotenv()

    parser = argparse.ArgumentParser()
    parser.add_argument("Path")
    args = parser.parse_args()
    Path = args.Path
    Path = Path + '/'

    bot_token = os.getenv('BOT_TOKEN')
    chat_id = os.getenv('CHAT_ID')
    hours_break = os.getenv('HOURS_BREAK')

    bot = telegram.Bot(token=bot_token)
    bot.token = bot._validate_token(bot_token)

    while True:
        upload_images_to_tg(Path, bot, chat_id)
        schedule.run_pending()
        time.sleep(int(hours_break)*60*60)
