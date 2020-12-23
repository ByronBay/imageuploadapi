import os

import requests


def upload_image(url="127.0.0.1", image_pfn="", data=""):
    print("url:       {}".format(url))
    print("image_pfn: {}".format(image_pfn))
    print("data:      {}".format(data))

    rv = 0

    try:

        # references to construction of this object:
        # how-to curl: https://stackoverflow.com/questions/12667797/using-curl-to-upload-post-data-with-files
        # curl to python : https://curl.trillworks.com/
        files = {
            'user_id': (None, '12345'),
            'installation_id': (None, 'abcdef_12345'),
            'image_1': (str(image_pfn), open(image_pfn, 'rb')),
            'image_2': (str(image_pfn), open(image_pfn, 'rb')),
        }

        rv = requests.post(url, files=files)

        print("request return value: {}".format(rv))

    except Exception as e:
        rv = e
        print(e)

    return rv


if __name__ == "__main__":
    url = "http://127.0.0.1:5000/api/v1/imageupload"

    image_filename = r"raspberry-pi-logo_resized_256.png"
    image_pfn = os.path.join("..", "data", image_filename)

    data = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }

    upload_image(url, image_pfn, data)
