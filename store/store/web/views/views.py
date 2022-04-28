from django.contrib.auth import mixins as auth_mixin, get_user_model
from django.views import generic as views
from store.web.models import Product, Order

UserModel = get_user_model()


class HomeView(views.TemplateView):
    template_name = 'web/home.html'


class DashboardView(auth_mixin.LoginRequiredMixin, views.ListView):
    model = Product
    template_name = 'web/dashboard.html'

    # context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        products = Product.objects.all()
        order, created = Order.objects.get_or_create(user=user, complete=False)
        items = order.orderitems_set.all()

        cart_items = order.get_cart_items()

        context['cart_items'] = cart_items
        context['products'] = products
        context['items'] = items
        context['order'] = order

        return context


class AboutUs(views.TemplateView):
    template_name = 'home_and_about_us/about_us.html'