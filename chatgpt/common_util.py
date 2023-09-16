#!/usr/bin/python3

import json
import os
from datetime import date


def get_date():
    return date.today()


def read_file_json(path):
    with open(path) as f:
        return json.load(f)


def read_file_lines(path):
    if not os.path.exists(path):
        return None

    with open(path, "r") as f:
        data_list = f.readlines()
    return data_list


def write_txt(path, data):
    with open(path, "w") as f:
        f.write(data)
