import os
from dotenv import load_dotenv
from instabot import Bot
import requests

load_dotenv()
IMAGE_DIRECTORY = os.getenv('IMAGE_DIRECTORY')

if not os.path.exists(IMAGE_DIRECTORY):
    raise NotADirectoryError(f'Image directory {IMAGE_DIRECTORY} not fount')


def download_image(image_url, image_name):
    image_file_name = os.path.join(IMAGE_DIRECTORY, image_name)
    response = requests.get(image_url)
    if not response.ok:
        return None
    with open(image_file_name, 'wb') as file:
        file.write(response.content)


def upload_images_to_instagram():
    load_dotenv()
    LOGIN = os.getenv('INSTAGRAM_LOGIN')
    PASSWORD = os.getenv('INSTAGRAM_PASSWORD')
    POSTED_IMAGES_FILE = 'posted_images.txt'

    bot = Bot()
    bot.login(username=LOGIN, password=PASSWORD)

    def post_image_to_instagram(image_name, caption=''):
        image_file_name = os.path.join(IMAGE_DIRECTORY, image_name)
        bot.upload_photo(image_file_name, caption=caption)

    try:
        with open(POSTED_IMAGES_FILE, 'r', encoding='utf8') as f:
            posted_images = f.read().splitlines()
    except FileNotFoundError:
        posted_images = []

    image_files = os.listdir(IMAGE_DIRECTORY)
    for image in image_files:
        if image not in posted_images:
            caption = os.path.splitext(image)[0]
            post_image_to_instagram(image, caption=caption)
            posted_images.append(image)

    with open(POSTED_IMAGES_FILE, 'w', encoding='utf8') as f:
        for image in posted_images:
            f.write(image + '\n')

