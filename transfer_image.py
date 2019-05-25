import os
from dotenv import load_dotenv
from instabot import Bot
import requests

load_dotenv()
images_directory = os.getenv('IMAGE_DIRECTORY')
os.makedirs(images_directory, exist_ok=True)

def download_image(image_url, image_name):
    image_file_name = os.path.join(images_directory, image_name)
    response = requests.get(image_url)
    with open(image_file_name, 'wb') as file:
        file.write(response.content)

def upload_images_to_instagram():
    load_dotenv()
    login = os.getenv('INSTAGRAM_LOGIN')
    password = os.getenv('INSTAGRAM_PASSWORD')
    posted_images_file = 'posted_images.txt'

    bot = Bot()
    bot.login(username=login, password=password)

    def post_image_to_instagram(image_name, caption=''):
        image_file_name = os.path.join(images_directory, image_name)
        bot.upload_photo(image_file_name, caption=caption)

    try:
        with open(posted_images_file, 'r', encoding='utf8') as f:
            posted_images = f.read().splitlines()
    except Exception:
        posted_images = []

    image_files = os.listdir(images_directory)
    for image in image_files:
        if image not in posted_images:
            caption = os.path.splitext(image)[0]
            post_image_to_instagram(image, caption=caption)
            posted_images.append(image)

    with open(posted_images_file, 'w', encoding='utf8') as f:
        for image in posted_images:
            f.write(image + '\n')

