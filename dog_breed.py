#!/usr/bin/env python

from typing import Final, List
import random
import urllib.request
import json
import argparse

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

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(
        prog="dog-breeds",
        description="a simple client for some dog-api endpoints",
        epilog="----------"
    )
    
    # push the command to `action` key stored in parsed args to know which sub parser is called
    sub_parsers = arg_parser.add_subparsers(dest="action")

    sub_list_all_parser = sub_parsers.add_parser("list-all", help="List all breeds")

    sub_get_image_parser = sub_parsers.add_parser("get-image", help="Get image of a breed, required arguments: --breed and --file")
    sub_get_image_parser.add_argument("-b", "--breed", required=True)
    sub_get_image_parser.add_argument("-f", "--file", required=True)

    args = vars(arg_parser.parse_args())

    # there should always be an "action" pair

    # Case 1: no command is called, print the help menu and quit
    if args["action"] is None:
        arg_parser.print_help()

    # Case 2: `list-all` command
    if args["action"] == "list-all":
        list_all()

    # Case 3: `get-image` command
    if args["action"] == "get-image":
        # Retrieve arguments (they are required)
        arg_breed = args["breed"]
        arg_filepath = args["file"]
        download_image(arg_breed, arg_filepath, None)
