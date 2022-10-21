import os
import random
import argparse

import telegram

from dotenv import load_dotenv
from os import listdir

from os.path import isfile
from os.path import join as joinpath


if __name__ == '__main__':
    load_dotenv()
    parser = argparse.ArgumentParser()
    parser.add_argument("img")
    parser.parse_args()
    args = parser.parse_args()
    img = args.img
    
    chat_id = os.environ['CHAT_ID']
    bot_token = os.environ['BOT_TOKEN']
    bot = telegram.Bot(token=bot_token)


    try:
        bot.send_document(chat_id=chat_id, document=open(img, 'rb'))
    except:
        print("No such file or directory")
        Path = 'test/'
        for image_file in listdir(Path):
            if isfile(joinpath(Path, image_file)):
                filesindir = os.listdir(Path)
                for files in filesindir:
                    random.shuffle(filesindir)
                    path_file = os.path.join(files)
        bot.send_document(chat_id=chat_id, document=open(Path + path_file, 'rb'))
