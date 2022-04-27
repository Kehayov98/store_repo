from datetime import date

from django.contrib.auth import get_user_model
from django.urls import reverse

from store.accounts.models import Profile
from django import test as django_test
UserModel = get_user_model()


class EditProfileViewTests(django_test.TestCase):
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

    def __get_response_for_profile(self, profile):
        return self.client.get(reverse('profile details', kwargs={'pk': profile.pk}))

    def __create_valid_user_and_profile(self):
        user = self.__create_user(**self.VALID_USER_CREDENTIALS)
        profile = Profile.objects.create(
            **self.VALID_PROFILE_DATA,
            user=user,
        )

        return (user, profile)

    # def test_profile_edit_success_url__expect_details_profile_page(self):
    #     _, profile = self.__create_valid_user_and_profile()
    #     credentials = {
    #         'username': 'testuser',
    #         'password': '12345qew',
    #     }
    #
    #     response = self.__get_response_for_profile(profile)
    #
    #     # self.assertTemplateUsed('accounts/profile_edit.html')
    #     self.assertRedirects(response, reverse('profile details'))