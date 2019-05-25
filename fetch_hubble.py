import requests
from transfer_image import download_image

hubble_api_url = 'http://hubblesite.org/api/v3'

def fetch_hubble_collection(collection_name='spacecraft'):

    def fetch_file_extension(link):
        extension = link.split('.')[-1]
        return extension

    def fetch_hubble_image(image_id, image_name):
        supported_file_types = ['jpeg', 'jpg', 'png']
        response = requests.get(f'{hubble_api_url}/image/{image_id}')
        image_url = response.json()['image_files'][-1]['file_url']
        file_extension = fetch_file_extension(image_url)
        if file_extension in supported_file_types:
            image_name = f'{image_name}.{file_extension}'
            download_image(image_url, image_name)

    payload = {
        'page': 'all',
        'collection_name': collection_name,
    }
    response = requests.get(f'{hubble_api_url}/images', data=payload)
    for image in response.json():
        fetch_hubble_image(image['id'], image['name'])



