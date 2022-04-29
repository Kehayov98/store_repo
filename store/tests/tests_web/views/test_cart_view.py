from datetime import date

from django import test as django_test
from django.contrib.auth import get_user_model
from django.urls import reverse

from store.accounts.models import Profile

UserModel = get_user_model()


class CartViewTest(django_test.TestCase):
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

    def __create_user(self, **credentials):
        return UserModel.objects.create_user(**credentials)

    def __create_valid_user_and_profile(self):
        user = self.__create_user(**self.VALID_USER_CREDENTIALS)
        profile = Profile.objects.create(
            **self.VALID_PROFILE_DATA,
            user=user,
        )

        return (user, profile)

    def test_when_opening_existing_product__expect_200(self):
        _, profile = self.__create_valid_user_and_profile()
        self.client.login(**self.VALID_USER_CREDENTIALS)

        response = self.client.get(reverse('cart'))

        self.assertEqual(200, response.status_code)

    def test_expect_correct_template(self):
        _, profile = self.__create_valid_user_and_profile()
        self.client.login(**self.VALID_USER_CREDENTIALS)
        self.client.get(reverse('cart'))

        self.assertTemplateUsed('cart_and_check_out/cart.html')
