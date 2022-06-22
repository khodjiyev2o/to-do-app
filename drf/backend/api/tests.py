from django.test import TestCase
from .models import Product
from django.contrib.auth.models import User
from django.test import Client
# Create your tests here.


class TodoTest(TestCase):
    def setup(self):
        obj1 = Product.objects.create(title='clean the house',completed=False)

    def test_request(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code,200)


    def test_request_api(self):
        client = Client()
        response = client.get('/api/task-list/')
        self.assertEqual(response.status_code, 200)
    