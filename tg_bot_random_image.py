import os
import time
import argparse
import logging

import telegram
from dotenv import load_dotenv

import image_files_listdir


def send_random_photo(bot, chat_id, path):
    file = image_files_listdir.get_random_file_from_dir(path)
    image_files_listdir.send_document(os.path.join(path, file), bot, chat_id)
    return True


def send_photo(bot, chat_id, img):
    filesindir = image_files_listdir.get_files_listdir(path)
    for file in filesindir:
        if file == img:
            image_files_listdir.send_document(
                os.path.join(path, file), bot, chat_id)
            return True


if __name__ == '__main__':
    load_dotenv()
    parser = argparse.ArgumentParser()
    parser.add_argument("--img", default=None,
                        help="The name of the image in the 'NASA' folder.")
    parser.add_argument("--path", default='images',
                        help="The folder name with images.")
    args = parser.parse_args()
    path = args.path
    img = args.img

    bot_token = os.environ['TG_BOT_TOKEN']
    chat_id = os.environ['TG_CHAT_ID']
    bot = telegram.Bot(token=bot_token)

    try:
        if not send_photo(bot, chat_id, img):
            logging.error(
                'Папки не существует или она пустая! Отправлено рандомное фото')
            send_random_photo(bot, chat_id, path='images')
    except (ConnectionError, RuntimeError, telegram.error.RetryAfter, telegram.error.NetworkError):
        time.sleep(60)
        send_random_photo(bot, chat_id, path='images')
