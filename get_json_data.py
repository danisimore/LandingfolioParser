import json
import requests

from get_landing_description import get_description


def get_data_file(request_headers):
    """Collect data and return a JSON file"""
    page = 1
    result_list = []

    while True:
        url = f"https://s3.landingfolio.com/inspiration?page={page}&sortBy=free-first"

        response = requests.get(url=url, headers=request_headers)
        data = response.json()

        for item in data:
            screenshots = item.get("screenshots")

            for screenshot in screenshots:
                image_url = screenshot["images"]["desktop"]
                screenshot["images"].update(
                    {"desktop": f"https://landingfoliocom.imgix.net/{image_url}"}
                )

            description = get_description(item.get("slug"))

            result_list.append(
                {
                    "title": item.get("title")
                    if item.get("title")[-1] != " "
                    else item.get("title")[:-1],
                    "url": item.get("url"),
                    "images": [
                        screenshot["images"]["desktop"]
                        for screenshot in item.get("screenshots")
                    ],
                    "description": description,
                }
            )

        if not data:
            with open("result_list.json", "a", encoding="utf-8") as file:
                json.dump(result_list, file, indent=4, ensure_ascii=False)

            return f"[INFO] Work finished"

        print(f"[+] Processed {page}")
        page += 1
