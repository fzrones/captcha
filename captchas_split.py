import os
import glob
from PIL import Image,ImageDraw
from ghelper import *


if __name__ == '__main__':
    # Get a list of all the captcha images we need to process
    captcha_image_files = glob.glob(os.path.join(CAPTCHA_IMAGE_FOLDER, "*"))
    # print(captcha_image_files)
    counts = {}
    # loop over the image paths
    for (i, captcha_image_file) in enumerate(captcha_image_files):
        print("[INFO] processing image {}/{}".format(i + 1, len(captcha_image_files)))

        # Since the filename contains the captcha text (i.e. "2A2X.png" has the text "2A2X"),
        # grab the base filename as the text
        filename = os.path.basename(captcha_image_file)
        captcha_correct_text = os.path.splitext(filename)[0]
        img = Image.open(captcha_image_file)
        img = two_value(img)
        clearNoise(img, 0, 3, 1)
        letter_image_regions = letter_split(img)
        for letter_bounding_box, letter_text in zip(letter_image_regions, captcha_correct_text):
            save_path = os.path.join(OUTPUT_FOLDER, letter_text)
            if not os.path.exists(save_path):
                os.makedirs(save_path)
            count = counts.get(letter_text, 1)
            p = os.path.join(save_path, "{}.jpeg".format(str(count).zfill(6)))
            letter_bounding_box.save(p)
            # increment the count for the current key
            counts[letter_text] = count + 1