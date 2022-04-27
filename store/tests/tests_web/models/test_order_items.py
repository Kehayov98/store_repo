from datetime import date

from django import test as django_test

from store.web.models import Product, OrderItems


class OrderItemsTest(django_test.TestCase):
    VALID_ORDER_ITEMS = {
        'quantity': 20,
        'date_added': date(1990, 5, 13),
    }

    VALID_PRODUCT_DATA = {
        'name': 'Test',
        'price': 10,
        'quantity': 10,
        'image': 'test.jpg',
        'description': 'Test for walk',
    }

    def test_cart_total_for_all_product(self):
        product = Product(**self.VALID_PRODUCT_DATA)

        order_items = OrderItems(
            **self.VALID_ORDER_ITEMS,
            product=product,
        )

        expected_total = 200

        self.assertEqual(expected_total, order_items.get_total)

    def test_cart_total__no_product__expect_zero(self):
        product = Product(**self.VALID_PRODUCT_DATA)

        order_items = OrderItems(
            quantity=0,
            date_added=self.VALID_ORDER_ITEMS['date_added'],
            product=product,
        )

        expected_total = 0

        self.assertEqual(expected_total, order_items.get_total)