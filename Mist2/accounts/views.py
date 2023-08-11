from django.shortcuts import render
from django.templatetags.static import static
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model, login, authenticate
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
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)

        # Authenticate and log in the user
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
        if user is not None:
            login(self.request, user)

        return response

class LoginForm(auth_forms.AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Username'}))
    password = forms.CharField(strip=False, widget=forms.PasswordInput(
        attrs={"autocomplete": 'current-password', 'placeholder': 'Password'}))
    success_url = reverse_lazy('home')


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'
    form_class = LoginForm


class LogoutUserView(auth_views.LogoutView):
    next_page = reverse_lazy('login')


class UserEditView(views.UpdateView):
    model = UserModel
    form_class = UserEditForm
    template_name = 'accounts/profile-edit-page.html'

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.object.pk})

    def get_object(self, queryset=None):
        return self.request.user


class ProfileDetailView(views.DetailView):
    template_name = 'accounts/profile-details-page.html'
    model = UserModel
    pk_url_kwarg = 'pk'


class ProfileDeleteView(views.DeleteView):
    template_name = 'accounts/profile-delete-page.html'
