import json

from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views import generic as views
import datetime

from django.contrib.auth import mixins as auth_mixin

from store.web.forms import CheckOutForm
from store.web.models import Order, Product, OrderItems


class CartView(auth_mixin.LoginRequiredMixin, views.TemplateView):
    template_name = 'cart_and_check_out/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        order, created = Order.objects.get_or_create(user=user, complete=False)
        items = order.orderitems_set.order_by('product__name')
        cart_items = order.get_cart_items()

        context['items'] = items
        context['order'] = order
        context['cart_items'] = cart_items

        return context


class CheckOutView(auth_mixin.LoginRequiredMixin, views.CreateView):
    form_class = CheckOutForm
    template_name = 'cart_and_check_out/check_out.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.order = Order.objects.get(user=form.instance.user, complete=False)
        user = self.request.user

        order = Order.objects.get(user=user, complete=False)
        order.complete = True
        order.transaction_id = datetime.datetime.now().timestamp()
        order_items = order.get_items

        for item in order_items:
            product = Product.objects.get(pk=item.product.pk)

            # if not check_product_availability(product.quantity, item.quantity):
            product.quantity -= item.quantity

            product.save()

        order.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        order, created = Order.objects.get_or_create(user=user, complete=False)
        items = order.orderitems_set.all()
        cart_items = order.get_cart_items()

        context['items'] = items
        context['order'] = order
        context['cart_items'] = cart_items

        return context


def update_item(request):
    data = json.loads(request.body)
    product_id = data['productId']
    action = data['action']

    user = request.user
    product = Product.objects.get(id=product_id)
    order, created = Order.objects.get_or_create(user=user, complete=False)

    order_item, created = OrderItems.objects.get_or_create(order=order, product=product)

    if action == 'add':
        order_item.quantity = (order_item.quantity + 1)
    elif action == 'remove':
        order_item.quantity = (order_item.quantity - 1)

    order_item.save()

    if order_item.quantity <= 0:
        order_item.delete()

    return JsonResponse('Item was added', safe=False)