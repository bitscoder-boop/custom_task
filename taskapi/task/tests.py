from rest_framework.test import APIClient
from django.test import TestCase
# from .models import User
import tempfile
from PIL import Image

# Create your tests here.


def temporary_image():
    """
    Returns a new temporary image file
    """

    image = Image.new('RGB', (100, 100))
    tmp_file = tempfile.NamedTemporaryFile(suffix='.jpg')
    image.save(tmp_file, 'jpeg')
    # important because after save(), the fp is already at the end of the file
    tmp_file.seek(0)
    return tmp_file


class UserApiTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_post_date(self):
        data = {
            'username': "dipesh",
            'description': "This is my description",
            'image': temporary_image(),
            'file': temporary_image()
        }
        response = self.client.post("/users", data=data)
        print(response.json())
        self.assertEqual(201, response.status_code)

    def test_get_all_users_return_empty_value(self):
        response = self.client.get('/users')
        self.assertEqual(200, response.status_code)
