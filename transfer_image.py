import os
from dotenv import load_dotenv
from instabot import Bot
import requests

load_dotenv()
IMAGE_DIRECTORY = os.getenv('IMAGE_DIRECTORY')
POSTED_IMAGES_FILE = os.getenv('POSTED_IMAGES_FILE')
INSTAGRAM_LOGIN = os.getenv('INSTAGRAM_LOGIN')
INSTAGRAM_PASSWORD = os.getenv('INSTAGRAM_PASSWORD')


def check_image_directory_exists():
    if not os.path.exists(IMAGE_DIRECTORY):
        raise NotADirectoryError(f'Image directory {IMAGE_DIRECTORY} not fount')


def download_image(image_url, image_name):
    check_image_directory_exists()
    image_file_name = os.path.join(IMAGE_DIRECTORY, image_name)
    response = requests.get(image_url)
    if not response.ok:
        return None
    with open(image_file_name, 'wb') as file:
        file.write(response.content)


def post_image_to_instagram(image_name, caption=''):
    check_image_directory_exists()
    bot = Bot()
    bot.login(username=INSTAGRAM_LOGIN, password=INSTAGRAM_PASSWORD)
    image_file_name = os.path.join(IMAGE_DIRECTORY, image_name)
    bot.upload_photo(image_file_name, caption=caption)


def get_posted_images():
    try:
        with open(POSTED_IMAGES_FILE, 'r', encoding='utf8') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []


def add_posted_images(posted_images):
    with open(POSTED_IMAGES_FILE, 'w', encoding='utf8') as f:
        for image in posted_images:
            f.write(image + '\n')


def upload_images_to_instagram():
    check_image_directory_exists()
    image_files = os.listdir(IMAGE_DIRECTORY)
    posted_images = get_posted_images()
    for image in image_files:
        if image not in posted_images:
            caption = os.path.splitext(image)[0]
            post_image_to_instagram(image, caption=caption)
            posted_images.append(image)
    add_posted_images(posted_images)



