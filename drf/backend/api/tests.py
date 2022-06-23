from django.test import TestCase
from .models import Product
from django.contrib.auth.models import User
from django.test import Client
# Create your tests here.
import os
import pathlib
import unittest
from selenium import webdriver

os.environ['PATH'] += r'C:\Users\django\selenium'


def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()


driver = webdriver.Chrome()


class Webpagetests(unittest.TestCase):

    def test_title(self):
        uri = file_uri('api/templates/sel.html')
        driver.get(uri)
        self.assertEqual(driver.title, 'TO DO')



class TodoTest(TestCase):
    def setup(self):
        obj1 = Product.objects.create(title='clean the house', completed=False)

    def test_request(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_request_api(self):
        client = Client()
        response = client.get('/api/task-list/')
        self.assertEqual(response.status_code, 200)
