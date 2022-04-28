from django.urls import path

from store.web.views.cart_and_check_out import CartView, CheckOutView, update_item, SuccessfulCheckOut
from store.web.views.product import CreateProductView, ProductDetailsView, EditProductView, DeleteProductView
from store.web.views.views import HomeView, DashboardView, AboutUs

urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    path('about_us/', AboutUs.as_view(), name='about us'),

    path('cart/', CartView.as_view(), name='cart'),
    path('checkout/', CheckOutView.as_view(), name='check out'),
    path('successful_check_out/', SuccessfulCheckOut.as_view(), name='successful check out'),
    path('update_item/', update_item, name='update item'),

    path('product_details/<int:pk>/', ProductDetailsView.as_view(), name='product details'),
    path('product_create/', CreateProductView.as_view(), name='product create'),
    path('product_edit/<int:pk>/', EditProductView.as_view(), name='product edit'),
    path('product_delete/<int:pk>/', DeleteProductView.as_view(), name='product delete')
]