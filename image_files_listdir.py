import os
import random


def get_files_listdir(path):
    return os.listdir(path)


def get_random_file_from_dir(path):
    return random.choice(os.listdir(path))


def send_document(file_path, bot, chat_id):
    with open(file_path, 'rb') as doc:
        bot.send_document(chat_id=chat_id, document=doc)
