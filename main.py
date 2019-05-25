from fetch_spacex import fetch_spacex_last_launch
from fetch_hubble import fetch_hubble_collection
from transfer_image import upload_images_to_instagram
import os
from dotenv import load_dotenv


if __name__ == '__main__':
    print('fetch_spacex_last_launch')
    fetch_spacex_last_launch()

    print('fetch_hubble_collection')
    collection_name = 'spacecraft'
    fetch_hubble_collection()

    print('upload_images_to_instagram')
    upload_images_to_instagram()
