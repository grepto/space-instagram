import requests
from download_image import download_image

hubble_api_url = 'http://hubblesite.org/api/v3/image'


def fetch_file_extension(link):
    extension = link.split('.')[-1]
    return extension


def fetch_hubble_image(image_id):
    response = requests.get(f'{hubble_api_url}/{image_id}')
    image_url = response.json()['image_files'][-1]['file_url']
    file_extension = fetch_file_extension(image_url)
    image_name = f'{image_id}.{file_extension}'
    download_image(image_url, image_name)

