import os
import json
import requests


def download_images(json_file_path):
    """Download images"""
    image_counter = 1
    try:
        with open(json_file_path, encoding="utf-8") as file:
            src = json.load(file)
    except Exception as _ex:
        print(_ex)
        return "[INFO] Check the file path!"

    for item in src:
        item_name = item.get("title")
        images_list = item.get("images")

        if not os.path.exists(f"data\\{item_name}"):
            os.mkdir(f"data\\{item_name}")

        for image_url in images_list:
            r = requests.get(url=image_url)

            with open(f"data\\{item_name}\\{image_counter}.png", "wb+") as file:
                file.write(r.content)
                image_counter += 1

                print(f"[+] Download")

    return "[INFO] Work finished!"
