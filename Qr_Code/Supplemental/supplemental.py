import validators

import os

def check_url(url: str):
    if validators.url(url):
        return True
    else:
        return False 


def replace_forward_slash(arg: str):
    return arg.replace("\\", "\\\\")


def check_filepath(file_path: str):
    return os.path.exists(file_path)