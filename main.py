from fetch_spacex import fetch_spacex_last_launch
from fetch_hubble import fetch_hubble_collection
from transfer_image import upload_images_to_instagram


if __name__ == '__main__':
    fetch_spacex_last_launch()

    collection_name = 'spacecraft'
    fetch_hubble_collection()

    print('upload_images_to_instagram')
    upload_images_to_instagram()
