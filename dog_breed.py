#!/usr/bin/env python

from typing import Final, List
import random
import urllib.request
import json

REMOTE_API_BASE: Final[str] = "https://dog.ceo/api/"
ENDPOINT_LIST_ALL: Final[str] = "breeds/list/all"

def __build_image_endpoint(breed: str):
    return f"breed/{breed}/images"


def __save_to_local_file(url: str, filename: str):
    urllib.request.urlretrieve(url, filename)
    return


def list_all():
    with urllib.request.urlopen(f"{REMOTE_API_BASE}{ENDPOINT_LIST_ALL}") as payload:
        decoded = json.load(payload)["message"]
        breeds = list(decoded.keys())

        for b in breeds:
            print(b)


def get_a_single_image(breed_name: str, img_no: int):
    try:
        with urllib.request.urlopen(f"{REMOTE_API_BASE}{__build_image_endpoint(breed_name)}") as payload:
            decoded = json.load(payload)["message"]
            img_list: List[str] = list(decoded)
            if img_no is not None:
                if 0 <= img_no < len(img_list):
                    return img_list[img_no]
            return random.choice(img_list)
    except urllib.request.HTTPError as e:
        if e.code == 404:
            return None
        else:
            raise NotImplementedError("Other error codes not implemented yet")

def download_image(breed_name: str, filename: str, img_no: int = None):
    # the download of image should be reworked, currently the img_no argument is simply ignored
    backend_name = breed_name.lower()
    img_url = get_a_single_image(backend_name, img_no)
    if img_url is None:
        print("There is no such breed in the database, skipping ...")
    else:
        __save_to_local_file(img_url, filename)