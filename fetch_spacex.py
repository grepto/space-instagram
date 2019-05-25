import requests
from download_image import download_image

spacex_api_url = 'https://api.spacexdata.com/v3/launches/66'


def fetch_spacex_last_launch():
    response = requests.get(spacex_api_url)
    image_links = response.json()['links']['flickr_images']
    for link_index, link in enumerate(image_links):
        image_name = f'spacex{link_index}.jpg'
        download_image(link, image_name)