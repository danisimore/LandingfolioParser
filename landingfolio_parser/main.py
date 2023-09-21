import time

from config import HEADERS
from download_images import download_images
from get_json_data import get_data_file


def main():
    start_time = time.time()

    print(get_data_file(request_headers=HEADERS))

    print(download_images("result_list.json"))

    finish_time = time.time() - start_time

    print(f"Worked time: {finish_time}")


if __name__ == "__main__":
    main()
