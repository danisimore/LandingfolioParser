import requests
from bs4 import BeautifulSoup


def get_description(slug):
    url = f"https://www.landingfolio.com/inspiration/post/{slug}"

    request = requests.get(url=url)

    detail_landing_page = request.text

    soup = BeautifulSoup(markup=detail_landing_page, features="html.parser")
    description = soup.find(
        name="p", attrs={"class": "text-base font-normal leading-7 text-gray-600"}
    )

    if description:
        return description.get_text().strip()
