from datetime import date

from django import test as django_test
from django.contrib.auth import get_user_model
from django.urls import reverse

from store.accounts.models import Profile

UserModel = get_user_model()


class UserLoginViewTests(django_test.TestCase):
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

    # def __get_response_for_profile(self, profile):
    #     return self.client.get(reverse('profile details', kwargs={'pk': profile.pk}))

    def __create_valid_user_and_profile(self):
        user = self.__create_user(**self.VALID_USER_CREDENTIALS)
        profile = Profile.objects.create(
            **self.VALID_PROFILE_DATA,
            user=user,
        )

        return (user, profile)

    def test_user_when__correct_is_active_expect_true(self):
        _, profile = self.__create_valid_user_and_profile()
        credentials = {
            'username': 'testuser',
            'password': '12345qew',
        }

        self.client.login(**credentials)

        response = self.client.get(reverse('index'))

        self.assertTrue(response.context['user'].is_active)

    def test_user_when__incorrect_is_active_expect_false(self):
        _, profile = self.__create_valid_user_and_profile()
        credentials = {
            'username': 'testuser1',
            'password': '12345qew',
        }

        self.client.login(**credentials)

        response = self.client.get(reverse('login user'))

        self.assertFalse(response.context['user'].is_active)

    def test_user_when__correct_template_login_expect_redirect_to_index(self):
        _, profile = self.__create_valid_user_and_profile()
        credentials = {
            'username': 'testuser',
            'password': '12345qew',
        }

        response = self.client.post(reverse('login user'), credentials)

        self.assertRedirects(response, reverse('index'), status_code=302, target_status_code=200)

