import requests
from keras.models import load_model
from helpers import resize_to_fit
from imutils import paths
import numpy as np
import cv2
import pickle
from PIL import Image
from ghelper import *
from download_captchas import download_images_to_folder

MODEL_FILENAME = "captcha_model.hdf5"
MODEL_LABELS_FILENAME = "model_labels.dat"
CAPTCHA_IMAGE_FOLDER = "generated_captcha_images"


with open(MODEL_LABELS_FILENAME, "rb") as f:
    lb = pickle.load(f)




model = load_model(MODEL_FILENAME)

# Grab some random CAPTCHA images to test against.
# In the real world, you'd replace this section with code to grab a real
# CAPTCHA image from a live website.
# captcha_image_files = np.random.choice(captcha_image_files, size=(10,), replace=False)

def ocr_image_to_label(text='0000'):
    download_images_to_folder(text=text,images_folder='temp')
    captcha_image_files = list(paths.list_images('temp'))
    # loop over the image paths
    # for image_file in captcha_image_files:
    image_file = 'temp/'+text+'.jpeg'
    img = Image.open(image_file)
    img = two_value(img)
    clearNoise(img, 0, 3, 1)
    letter_image_regions = letter_split(img)
    # [letter_image_regions[i].save(str(i+1))+'.jpeg' for i in range(4)]
    [letter_image_regions[i].save(str(i + 1) + '.jpeg') for i in range(4)]

    predictions = []

    # loop over the lektters
    for i in range(4):
        # Grab the coordinates of the letter in the image
        # x, y, w, h = letter_bounding_box

        # Extract the letter from the original image with a 2-pixel margin around the edge
        # letter_image = image[y - 2:y + h + 2, x - 2:x + w + 2]
        letter_bounding_box = cv2.imread(str(i + 1) + '.jpeg')
        letter_bounding_box = cv2.cvtColor(letter_bounding_box, cv2.COLOR_BGR2GRAY)
        letter_image = resize_to_fit(letter_bounding_box, 20, 20)

        # Turn the single image into a 4d list of images to make Keras happy
        letter_image = np.expand_dims(letter_image, axis=2)
        letter_image = np.expand_dims(letter_image, axis=0)

        # Ask the neural network to make a prediction
        prediction = model.predict(letter_image)

        # Convert the one-hot-encoded prediction back to a normal letter
        letter = lb.inverse_transform(prediction)[0]
        predictions.append(letter)

    # Print the captcha's text
    captcha_text = "".join(predictions)
    return captcha_text

if __name__ == '__main__':
    print(ocr_image_to_label(text='5467'))