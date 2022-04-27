from django.core.exceptions import ValidationError


def validate_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError('Value must contain only letters')


def username_validator_only_digit_and_letters(value):
    for symbol in value:
        if not symbol.isalpha() or not symbol.isdigit():
            raise ValidationError('Value must contain letters or digits only')


def check_product_availability(product_in_warehouse, order_stock):
    if product_in_warehouse < order_stock:
        raise LookupError("We didn't have enough stock for this medicine")

# def quantity_cant_be_negative(value):
#     if value < 0:
#         raise ValidationError('Value ')