import sys
sys.path.append("C:\\Users\\kimst\\Documents\\Python_Projects")
from Qr_Code.src.qr_generator import Qr_Generator
import pytest
import os


def test_get_URL_google():
    url = "https://www.google.com"
    file = r"C:\\Users\\kimst\\Desktop"
    name = "google"
   
    q = Qr_Generator(url, file, name)
    print(f"{q.get_url}")
    assert url == q.get_url()

def test_get_file_location():
    url = "https://www.google.com"
    file = r"C:\\Users\\kimst\\Desktop"
    name = "google"   
    q = Qr_Generator(url, file, name)
    print(q.get_location())
    assert file == q.get_location()

def test_get_file_name_with_google():
    url = "https://www.google.com"
    file = r"C:\\Users\\kimst\\Desktop"
    name = "google"
   
    q = Qr_Generator(url, file, name)

    assert name == q.get_filename()