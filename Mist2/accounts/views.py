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
    template_name = 'accounts/register-page.html'  # TODO: Add template
    success_url = reverse_lazy('home')


class LoginForm(auth_forms.AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Username'}))
    password = forms.CharField(strip=False, widget=forms.PasswordInput(
        attrs={"autocomplete": 'current-password', 'placeholder': 'Password'}))


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'
    form_class = LoginForm


class LogoutUserView(auth_views.LogoutView):
    next_page = reverse_lazy('login')


class UserEditView(views.UpdateView):
    model = UserModel
    form_class = UserEditForm
    template_name = ''  # TODO: Add template

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.object.pk})


class ProfileDetailView(views.DetailView):
    template_name = 'accounts/profile-details-page.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        profile_image = static('images/person.png')

        if self.object.profile_picture is not None:
            profile_image = self.object.profile_picture

        context = super().get_context_data(**kwargs)

        # context['pets_photos'] = self.request.photo_set.all()

        return context


class ProfileDeleteView(views.DeleteView):
    template_name = 'accounts/profile-delete-page.html'
