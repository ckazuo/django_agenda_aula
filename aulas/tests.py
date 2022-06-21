from django.test import TestCase
import unittest
from django.test import Client

# Create your tests here.
class SimpleTest(unittest.TestCase):
    def setUp(self) -> None:
        self.client = Client()
        return super().setUp()

    def test_indexpageresponse(self):

        # Issue a GET request.
        response = self.client.get('index')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
