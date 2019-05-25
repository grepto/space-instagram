import requests
import os

directory = 'images'
os.makedirs(directory, exist_ok=True)


def download_image(image_url, image_name):
    image_file = os.path.join(directory, image_name)
    response = requests.get(image_url)
    with open(image_file, 'wb') as file:
        file.write(response.content)
