import random
from imutils import paths
from os import path
import requests
from PIL import Image

CAPTCHAS_IMAGES_FOLDER = 'generated_captcha_images'


def download_images_to_folder(url = 'http://www.7xiwang.com/WebService/ImageValidateCode?code=',text='0000',images_folder=CAPTCHAS_IMAGES_FOLDER):
    image_source = requests.get(url+text).content
    with open(path.join(images_folder,text+'.jpeg'),'wb') as pic:
        pic.write(image_source)


if __name__ == '__main__':
    for i in range(10000):
        text = str(i).zfill(4)
        download_images_to_folder(text=text)