from django import forms
from django.shortcuts import render
from django.contrib.auth import views as auth_views

from django.urls import reverse_lazy
from django.views import generic as views

from store.accounts.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from store.accounts.models import Profile
from store.common.view_mixin import RedirectToDashboard


class UserRegisterView(RedirectToDashboard, views.CreateView):
    form_class = CreateProfileForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login user')


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login_page.html'
    success_url = reverse_lazy('index')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class EditProfileView(views.UpdateView):
    model = Profile
    template_name = 'accounts/profile_edit.html'
    form_class = EditProfileForm

    def get_success_url(self):
        return reverse_lazy('profile details', kwargs={'pk': self.object.pk})


class ProfileDetailView(views.DetailView):
    model = Profile
    template_name = 'accounts/profile.html'

    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.object.user_id == self.request.user.id
        # context['is_super_user'] = self.object.user_id == self.request.user.id

        return context


class ProfileDeleteView(views.DeleteView):
    model = Profile
    template_name = 'accounts/profile_delete.html'
    form_class = DeleteProfileForm

    def get_success_url(self):
        return reverse_lazy('index')

