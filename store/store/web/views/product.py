from django.urls import reverse_lazy
from django.views import generic as views

from store.web.forms import CreateProductFrom, EditProductForm, DeleteProductForm
from store.web.models import Product, Order

from django.contrib.auth import mixins as auth_mixin


class ProductDetailsView(views.DetailView):
    model = Product
    template_name = 'product/product_details.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        order, create = Order.objects.get_or_create(user=self.request.user, complete=False)

        cart_items = order.get_cart_items()

        context['cart_items'] = cart_items

        return context


class CreateProductView(auth_mixin.LoginRequiredMixin, auth_mixin.PermissionRequiredMixin, views.CreateView):
    template_name = 'product/product_create.html'
    form_class = CreateProductFrom

    success_url = reverse_lazy('dashboard')
    permission_required = ('web.add_product')


class EditProductView(auth_mixin.LoginRequiredMixin, auth_mixin.PermissionRequiredMixin, views.UpdateView):
    model = Product
    template_name = 'product/product_edit.html'
    form_class = EditProductForm
    permission_required = ('web.change_product')

    def get_success_url(self):
        return reverse_lazy('product details', kwargs={'pk': self.object.pk})


class DeleteProductView(auth_mixin.LoginRequiredMixin, auth_mixin.PermissionRequiredMixin, views.DeleteView):
    model = Product
    form_class = DeleteProductForm
    template_name = 'product/product_delete.html'

    success_url = reverse_lazy('dashboard')
    permission_required = ('web.delete_product')

