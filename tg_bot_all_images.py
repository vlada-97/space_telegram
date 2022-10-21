import os
import argparse
import random
import time

from os import listdir
from os.path import isfile
from os.path import join as joinpath

import schedule
import telegram
from dotenv import load_dotenv


def upload_images_to_tg(Path, bot_obj):
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
    parser.add_argument("path")
    parser.parse_args()
    args = parser.parse_args()
    Path = args.path
    
    bot_token = os.environ['BOT_TOKEN']
    bot = telegram.Bot(token=bot_token)
    chat_id = os.environ['CHAT_ID']
    hours_break = os.environ['HOURS_BREAK']

    while True:
        upload_images_to_tg(Path, bot)
        schedule.run_pending()
        time.sleep(int(hours_break)*60)
