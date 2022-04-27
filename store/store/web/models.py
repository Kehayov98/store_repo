from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

from store.common.validators import check_product_availability

UserModel = get_user_model()


class Category(models.Model):
    NIKE = 'Nike'
    ADIDAS = 'Adidas'
    JORDAN = 'Jordan'
    VANS = 'Vans'
    PUMA = 'Puma'
    KAPPA = 'Kappa'
    UNDER_ARMOUR = 'Under Armour'
    TIMBERLAND = 'Timberland'

    BRAND = [(x, x) for x in (NIKE, ADIDAS, JORDAN, VANS, PUMA, KAPPA, UNDER_ARMOUR, TIMBERLAND)]

    name = models.CharField(
        max_length=max(len(x) for x, _ in BRAND),
        choices=BRAND
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    PRODUCT_MAX_LENGTH = 35
    PRODUCT_MIN_LENGTH = 2
    PRODUCT_MIN_QUANTITY = 0

    SHOES_PHOTO_PATH = 'shoes'

    name = models.CharField(
        max_length=PRODUCT_MAX_LENGTH
    )

    price = models.FloatField()

    quantity = models.IntegerField(
        validators=(
            MinValueValidator(PRODUCT_MIN_QUANTITY),
        )
    )

    image = models.ImageField(
        blank=True,
        null=True,
        upload_to=SHOES_PHOTO_PATH,
    )

    description = models.TextField()

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Order(models.Model):
    date_order = models.DateTimeField(
        auto_now_add=True,

    )

    complete = models.BooleanField(
        default=False,
        null=True,
        blank=False,
    )

    transaction_id = models.CharField(
        max_length=200,
        null=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    # @property
    # def set_order_true(self):
    #     return self.complete == True

    @property
    def get_cart_total(self):
        order_items = self.orderitems_set.all()

        total = sum([item.get_total for item in order_items])
        return total

    def get_cart_items(self):
        order_items = self.orderitems_set.all()

        total = sum([item.quantity for item in order_items])
        return total

    @property
    def get_items(self):
        return self.orderitems_set.all()

    def __str__(self):
        return str(self.id)


class OrderItems(models.Model):
    DEFAULT_QUANTITY = 0

    quantity = models.IntegerField(
        default=DEFAULT_QUANTITY,
        null=True,
        blank=True,
    )

    date_added = models.DateTimeField(
        auto_now_add=True,
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    @property
    def get_total(self):
        total = self.product.price * self.quantity

        return total


class ShippingAddress(models.Model):
    ADDRESS_MAX_LENGTH = 200
    CITY_MAX_LENGTH = 50
    STATE_MAX_LENGTH = 100
    ZIP_CODE_MAX_LENGTH = 200

    address = models.CharField(
        max_length=ADDRESS_MAX_LENGTH,
        null=True,
    )

    city = models.CharField(
        max_length=CITY_MAX_LENGTH,
        null=True,
    )

    state = models.CharField(
        max_length=STATE_MAX_LENGTH,
        null=True,
    )

    zipcode = models.CharField(
        max_length=ZIP_CODE_MAX_LENGTH,
        null=True,
    )

    date_added = models.DateTimeField(
        auto_now_add=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    order = models.ForeignKey(
        Order,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.address
