from django.urls import path

from store.web.views.product import CreateProductView, ProductDetailsView, EditProductView, DeleteProductView
from store.web.views.views import HomeView, DashboardView, CartView, CheckOutView, update_item

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    path('cart/', CartView.as_view(), name='cart'),
    path('checkout/', CheckOutView.as_view(), name='check out'),
    path('update_item/', update_item, name='update item'),

    path('product_details/<int:pk>/', ProductDetailsView.as_view(), name='product details'),
    path('product_create/', CreateProductView.as_view(), name='product create'),
    path('product_edit/<int:pk>/', EditProductView.as_view(), name='product edit'),
    path('product_delete/<int:pk>/', DeleteProductView.as_view(), name='product delete')
]