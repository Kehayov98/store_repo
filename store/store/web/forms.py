from django import forms
from django.contrib.auth import get_user_model

from store.common.view_mixin import BootstrapFormMixin, DisabledFieldsFormMixin
from store.web.models import ShippingAddress, Order, Product

UserModel = get_user_model()


class CheckOutForm(forms.ModelForm):

    class Meta:
        model = ShippingAddress

        fields = ('address', 'city', 'state', 'zipcode', )

        widgets = {
            'address': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Address'
                }
            ),

            'city': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter City'
                }
            ),

            'state': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter State'
                }
            ),

            'zipcode': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter Zipcode'
                }
            ),
        }


class CreateProductFrom(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Product

        fields = '__all__'


class EditProductForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Product

        fields = '__all__'


class DeleteProductForm(BootstrapFormMixin, forms.ModelForm):
    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Product

        fields = ()