import sys
sys.path.append("C:\\Users\\kimst\\Documents\\Python_Projects")
from Qr_Code.src.qr_generator import Qr_Generator
import pytest
import os

url = "https://www.google.com"
file = r"C:\\Users\\kimst\\Desktop"
name = "google"

q = Qr_Generator(url, file, name)
def test_get_URL_google(url=url):
    assert url == q.get_url()


filepath = f"{file}\\{name}.png"
def test_get_file_location(filepath=filepath):
    assert filepath == q.get_location()

def test_get_file_name_with_google(name=name):
    assert name == q.get_filename()