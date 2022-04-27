from django import test as django_test

from store.web.models import Product


class ProductTest(django_test.TestCase):
    VALID_PRODUCT_DATA = {
        'name': 'Test',
        'price': 11.5,
        'quantity': 20,
        'image': 'test.jpg',
        'description': 'Test for walk',
    }

    def test_str__expect_to_return_name(self):
        product = Product(**self.VALID_PRODUCT_DATA)
        
        expected_str = 'Test'

        self.assertEqual(expected_str, product.__str__())