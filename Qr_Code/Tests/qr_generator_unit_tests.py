import sys
sys.path.append("C:\\Users\\kimst\\Documents\\Python_Projects")
from Qr_Code.src.qr_generator import Qr_Generator
import pytest
import os

url = "https://www.google.com"
file = r"C:\\Users\\kimst\\Desktop"
name = "google"
file_format =".png"
q = Qr_Generator(url, file, name)
def test_get_URL_google(url=url):
    assert url == q.get_url()


filepath = f"{file}\\{name}{file_format}"
def test_get_file_location(filepath=filepath):
    assert filepath == q.get_save_location_path()

def test_get_file_name_with_google(name=name):
    assert name == q.get_filename()

def test_QR_Generator_type():
    assert type(q) == Qr_Generator

def test_save_directory():
    assert q.get_save_diractory() == file
 

def confirm_file_creation():
    q.make_qr()
    assert os.Path.exists(q.get_save_location_path())