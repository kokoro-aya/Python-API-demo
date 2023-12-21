#!/usr/bin/env python

from typing import Final


REMOTE_API_BASE: Final[str] = "https://dog.ceo/api/"
ENDPOINT_LIST_ALL: Final[str] = "breeds/list/all"

def __build_image_endpoint(breed: str):
    pass


def __save_to_local_file(url: str, filename: str):
    pass


def list_all():
    pass


def get_a_single_image(breed_name: str, img_no: int):
    pass

def download_image(breed_name: str, filename: str, img_no: int = None):
    pass