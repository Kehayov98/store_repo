from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from store.accounts.views import UserLoginView, UserRegisterView, ProfileDetailView, EditProfileView, ProfileDeleteView, \
    ChangeUserPasswordView, SuccessfulRegister

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login user'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('successful_register/', SuccessfulRegister.as_view(), name='successful register'),
    path('logout/', auth_views.LogoutView.as_view(template_name=reverse_lazy('accounts/login user')), name='logout'),

    path('chanage_password/<int:pk>/', ChangeUserPasswordView.as_view(), name='change password'),
    path('password_change_done/', RedirectView.as_view(url=reverse_lazy('dashboard')), name='password_change_done'),

    path('edit_profile/<int:pk>/', EditProfileView.as_view(), name='edit profile'),
    path('delete_profile/<int:pk>/', ProfileDeleteView.as_view(), name='delete profile'),

    path('<int:pk>/', ProfileDetailView.as_view(), name='profile details')
]
