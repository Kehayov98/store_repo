from datetime import date

from django import test as django_test
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from store.accounts.models import Profile


UserModel = get_user_model()


class ProfileTest(django_test.TestCase):
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

    def test_profile_create__when_first_name_contains_only_letters__expect_success(self):
        _, profile = self.__create_valid_user_and_profile()

        profile.save()

        self.assertIsNotNone(profile.pk)

    def test_profile_create__when_first_name_contains_a_digit__expect_to_fail(self):
        first_name = 'Alexander1'
        user = self.__create_user(**self.VALID_USER_CREDENTIALS)

        profile = Profile(
            first_name=first_name,
            last_name=self.VALID_PROFILE_DATA['last_name'],
            date_of_birth=self.VALID_PROFILE_DATA['date_of_birth'],
            email=self.VALID_PROFILE_DATA['email'],
            gender=self.VALID_PROFILE_DATA['gender'],
            user=user,
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)

    def test_profile_create__when_first_name_contains_a_dollar_sigh__expect_to_fail(self):
        first_name = 'Alexand$er'
        user = self.__create_user(**self.VALID_USER_CREDENTIALS)

        profile = Profile(
            first_name=first_name,
            last_name=self.VALID_PROFILE_DATA['last_name'],
            date_of_birth=self.VALID_PROFILE_DATA['date_of_birth'],
            email=self.VALID_PROFILE_DATA['email'],
            gender=self.VALID_PROFILE_DATA['gender'],
            user=user,
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)

    def test_profile_create__when_first_name_contains_a_space__expect_to_fail(self):
        first_name = 'Alexan der'
        user = self.__create_user(**self.VALID_USER_CREDENTIALS)

        profile = Profile(
            first_name=first_name,
            last_name=self.VALID_PROFILE_DATA['last_name'],
            date_of_birth=self.VALID_PROFILE_DATA['date_of_birth'],
            email=self.VALID_PROFILE_DATA['email'],
            gender=self.VALID_PROFILE_DATA['gender'],
            user=user,
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)

    def test_profile_create__when_last_name_contains_a_digit__expect_to_fail(self):
        last_name = 'Kehayov2'
        user = self.__create_user(**self.VALID_USER_CREDENTIALS)

        profile = Profile(
            first_name=self.VALID_PROFILE_DATA['first_name'],
            last_name=last_name,
            date_of_birth=self.VALID_PROFILE_DATA['date_of_birth'],
            email=self.VALID_PROFILE_DATA['email'],
            gender=self.VALID_PROFILE_DATA['gender'],
            user=user,
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)

    def test_profile_create__when_last_name_contains_a_dollar_sigh__expect_to_fail(self):
        last_name = 'Kehayov$'
        user = self.__create_user(**self.VALID_USER_CREDENTIALS)

        profile = Profile(
            first_name=self.VALID_PROFILE_DATA['first_name'],
            last_name=last_name,
            date_of_birth=self.VALID_PROFILE_DATA['date_of_birth'],
            email=self.VALID_PROFILE_DATA['email'],
            gender=self.VALID_PROFILE_DATA['gender'],
            user=user,
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)

    def test_profile_create__when_last_name_contains_a_space__expect_to_fail(self):
        last_name = 'Kehayo v'
        user = self.__create_user(**self.VALID_USER_CREDENTIALS)

        profile = Profile(
            first_name=self.VALID_PROFILE_DATA['first_name'],
            last_name=last_name,
            date_of_birth=self.VALID_PROFILE_DATA['date_of_birth'],
            email=self.VALID_PROFILE_DATA['email'],
            gender=self.VALID_PROFILE_DATA['gender'],
            user=user,
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)

    def test_profile_full_name__when_valid__expect_correct_full_name(self):
        profile = Profile(**self.VALID_PROFILE_DATA)

        expected_full_name = f"{self.VALID_PROFILE_DATA['first_name']} {self.VALID_PROFILE_DATA['last_name']}"

        self.assertEqual(expected_full_name, profile.get_full_name)

    def test_profile_return_str_with__correct_date(self):
        profile = Profile(**self.VALID_PROFILE_DATA)

        expected_str = 'Test User'
        self.assertEqual(expected_str, profile.__str__())