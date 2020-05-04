from django.test import TestCase
from .models import Product

# Create your tests here.


class ProductTest(TestCase):
    """
    Defining test , we will run for Post Model
    """
    def test_str(self):
        test_name = Product(name='A Product')
        self.assertEqual(str(test_name), 'A Product')
