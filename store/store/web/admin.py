from django.contrib import admin

# Register your models here.
from store.web.models import Product, ShippingAddress, OrderItems, Order, Category


class ProductInlineAdmin(admin.StackedInline):
    model = Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image', 'quantity', 'description', 'category_id')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_order', 'complete', 'transaction_id')


@admin.register(OrderItems)
class OrderItemsAdmin(admin.ModelAdmin):
    list_display = ('quantity', 'date_added', 'product', 'order')


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'city', 'state', 'zipcode', 'date_added', 'order' )
