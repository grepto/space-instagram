import requests
import os
from transfer_image import download_image
from dotenv import load_dotenv

load_dotenv()
HUBBLE_API_URL = os.getenv('HUBBLE_API_URL')


def fetch_file_extension(link):
    return os.path.splitext(link)[1][1:]


def fetch_hubble_image(image_id, image_name):
    supported_file_types = ['jpeg', 'jpg', 'png']
    response = requests.get(f'{HUBBLE_API_URL}/image/{image_id}')
    if not response.ok:
        return None
    image_url = response.json()['image_files'][-1]['file_url']
    file_extension = fetch_file_extension(image_url)
    if file_extension in supported_file_types:
        image_name = f'{image_name}.{file_extension}'
        download_image(image_url, image_name)


def fetch_hubble_collection(collection_name='spacecraft'):
    payload = {
        'page': 'all',
        'collection_name': collection_name,
    }
    response = requests.get(f'{HUBBLE_API_URL}/images', data=payload)
    if not response.ok:
        return None
    for image in response.json():
        fetch_hubble_image(image['id'], image['name'])



