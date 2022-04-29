from datetime import date

from django.test import RequestFactory
from django import test as django_test
from django.contrib.auth import get_user_model
from django.urls import reverse

from store.accounts.models import Profile
from store.web.models import Product, Category
from store.web.views.product import ProductDetailsView

UserModel = get_user_model()


class ProductDetailsViewTest(django_test.TestCase):
    VALID_USER_CREDENTIALS = {
        'username': 'testuser',
        'password': '12345qew',
    }

    VALID_PROFILE_DATA = {
        'first_name': 'Test',
        'last_name': 'User',
        'date_of_birth': date(1990, 4, 13),
        'email': 'testmail@abv.bg',
        'gender': 'Male',
    }

    VALID_PRODUCT_DATA = {
        'name': 'Test',
        'price': 11.5,
        'quantity': 20,
        'image': 'test.jpg',
        'description': 'Test for walk',
    }

    VALID_CATEGORY_DATA = {
        'name': 'Nike'
    }

    def __create_user(self, **credentials):
        return UserModel.objects.create_user(**credentials)

    def __get_response_for_product(self, product):
        return self.client.get(reverse('product details', kwargs={'pk': product.pk}))

    def __create_valid_user_and_profile(self):
        user = self.__create_user(**self.VALID_USER_CREDENTIALS)
        profile = Profile.objects.create(
            **self.VALID_PROFILE_DATA,
            user=user,
        )

        return (user, profile)

    def __create_category(self):
        return Category(**self.VALID_CATEGORY_DATA)

    def __create_product(self):
        return Product(
            **self.VALID_PRODUCT_DATA,
        )

    def test_when_opening_not_existing_product__expect_404(self):
        _, profile = self.__create_valid_user_and_profile()
        self.client.login(**self.VALID_USER_CREDENTIALS)

        response = self.client.get(reverse('product details', kwargs={
            'pk': 1,
        }))

        self.assertEqual(404, response.status_code)

    def test_when_opening_existing_product__expect_200(self):
        _, profile = self.__create_valid_user_and_profile()
        self.client.login(**self.VALID_USER_CREDENTIALS)

        category = self.__create_category()
        category.save()

        product = Product(
            **self.VALID_PRODUCT_DATA,
            category=category,
        )
        product.save()

        response = self.__get_response_for_product(product)

        self.assertEqual(200, response.status_code)

    def test_expect_correct_template(self):
        _, profile = self.__create_valid_user_and_profile()
        self.client.login(**self.VALID_USER_CREDENTIALS)

        category = self.__create_category()
        category.save()

        product = Product(
            **self.VALID_PRODUCT_DATA,
            category=category,
        )
        product.save()

        self.__get_response_for_product(product)

        self.assertTemplateUsed('product/product_details.html')

    # def test_context_date(self):
    #     _, profile = self.__create_valid_user_and_profile()
    #     self.client.login(**self.VALID_USER_CREDENTIALS)
    #
    #     category = self.__create_category()
    #     category.save()
    #
    #     product = Product(
    #         **self.VALID_PRODUCT_DATA,
    #         category=category,
    #     )
    #     product.save()
    #
    #     response = self.client.get(reverse('product details', kwargs={'pk': product.pk}))
    #     self.assertIn('environment', response.context)