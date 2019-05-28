import requests
from transfer_image import download_image
from dotenv import load_dotenv
import os

load_dotenv()
SPACEX_API_URL = os.getenv('SPACEX_API_URL')


def fetch_spacex_last_launch():
    response = requests.get(SPACEX_API_URL)
    if not response.ok:
        return None
    image_links = response.json()['links']['flickr_images']
    for link_index, link in enumerate(image_links):
        image_name = f'spacex{link_index}.jpg'
        download_image(link, image_name)