from datetime import date

from django import test as django_test

from store.web.models import ShippingAddress


class ShippingAddressTest(django_test.TestCase):
    VALID_SHIPPING_ADDRESS_DATA = {
        'address': 'Test address',
        'city': 'Test',
        'state': 'Test',
        'zipcode': '100',
        'date_added': date(2020, 5, 11),
    }

    def __create_valid_shipping_address(self):
        return ShippingAddress(**self.VALID_SHIPPING_ADDRESS_DATA)

    def test_str_return_address(self):
        shipping_address = self.__create_valid_shipping_address()

        expected_address = 'Test address'

        self.assertEqual(expected_address, shipping_address.address)