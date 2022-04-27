from datetime import date

from django import test as django_test
from django.contrib.auth import get_user_model

from store.web.models import Product, Order, OrderItems, Category

UserModel = get_user_model()


class OrderTest(django_test.TestCase):
    VALID_USER_CREDENTIALS = {
        'username': 'testuser',
        'password': '12345qew',
    }

    VALID_ORDER_DATA = {
        'date_order': date(1990, 4, 13),
    }

    VALID_CATEGORY_DATA = {
        'name': 'Nike'
    }

    VALID_PRODUCT_DATA = {
        'name': 'Test',
        'price': 10,
        'quantity': 10,
        'image': 'test.jpg',
        'description': 'Test for walk',
    }

    VALID_ORDER_ITEMS = {
        'quantity': 20,
        'date_added': date(1990, 5, 13),
    }

    def __create_user(self, **credentials):
        return UserModel.objects.create_user(**credentials)

    def __create_valid_order(self):
        user = self.__create_user(**self.VALID_USER_CREDENTIALS)
        return Order(
            **self.VALID_ORDER_DATA,
            user=user,
        )

    def __create_category(self):
        return Category(**self.VALID_CATEGORY_DATA)

    def __create_product(self):
        return Product(
            **self.VALID_PRODUCT_DATA,
        )

    def __create_order_items(self):
        return OrderItems(
            self.VALID_ORDER_ITEMS,
        )

    def test_cart_items_quantity(self):
        order = self.__create_valid_order()
        order.save()

        category = self.__create_category()
        category.save()

        product = Product(
            **self.VALID_PRODUCT_DATA,
            category=category,
        )
        product.save()

        order_items = OrderItems(
            **self.VALID_ORDER_ITEMS,
            order=order,
            product=product,
        )
        order_items.save()

        expected_quantity = 20

        self.assertEqual(expected_quantity, order_items.order.get_cart_items())

    def test_cart_total_items(self):
        order = self.__create_valid_order()
        order.save()

        category = self.__create_category()
        category.save()

        product = Product(
            **self.VALID_PRODUCT_DATA,
            category=category,
        )
        product.save()

        order_items = OrderItems(
            **self.VALID_ORDER_ITEMS,
            order=order,
            product=product,
        )
        order_items.save()

        expected_total = 200

        self.assertEqual(expected_total, order_items.order.get_cart_total)

    def test_str_expect_return_id_as_str(self):
        order = self.__create_valid_order()
        order.save()

        expected_str = '3'

        self.assertEqual(expected_str, order.__str__())