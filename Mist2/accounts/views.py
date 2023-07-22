from django.shortcuts import render
from django.templatetags.static import static
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model
from django.contrib.auth import forms as auth_forms
from django.contrib.auth.forms import UsernameField
from django import forms

from Mist2.accounts.models import MistUser, UserEditForm

UserModel = get_user_model()


class RegisterUserForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email')


class RegisterUserView(views.CreateView):
    form_class = RegisterUserForm
    template_name = ''  # TODO: Add template
    success_url = reverse_lazy('login')


class LoginForm(auth_forms.AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Username'}))
    password = forms.CharField(strip=False, widget=forms.PasswordInput(
        attrs={"autocomplete": 'current-password', 'placeholder': 'Password'}))


class LoginUserView(auth_views.LoginView):
    template_name = ''  # TODO: Add template
    form_class = LoginForm


class LogoutUserView(auth_views.LogoutView):
    next_page = reverse_lazy('login')


class UserEditView(views.UpdateView):
    model = UserModel
    form_class = UserEditForm
    template_name = ''  # TODO: Add template

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.object.pk})