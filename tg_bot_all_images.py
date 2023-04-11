import os
import time
import argparse
import logging

import telegram
from dotenv import load_dotenv

import image_files_listdir


def upload_images_to_tg(path, bot, chat_id, hours_break):
    filesindir = image_files_listdir.get_files_listdir(path)
    for file in filesindir:
        image_files_listdir.send_document(
            os.path.join(path, file), bot, chat_id)
        time.sleep(hours_break*60*60)


if __name__ == '__main__':
    load_dotenv()
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", default='images',
                        help="Path to the photo folder")
    parser.add_argument("--hours", default=4, type=int,
                        help="Bot work break hours.")
    args = parser.parse_args()
    path = args.path
    hours_break = args.hours

    bot_token = os.environ['TG_BOT_TOKEN']
    chat_id = os.environ['TG_CHAT_ID']
    bot = telegram.Bot(token=bot_token)

    while True:
        try:
            upload_images_to_tg(path, bot, chat_id, hours_break)
        except (ConnectionError, RuntimeError, telegram.error.RetryAfter, telegram.error.NetworkError) as ex:
            logging.error(ex)
            time.sleep(60)
        except FileNotFoundError as ex:
            logging.error(ex)
            break
