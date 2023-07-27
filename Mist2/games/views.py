from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Game


# Create your views here.

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('name', 'genre', 'game_photo', 'size', 'price', 'description')
        labels = {
            'name': 'Name of the game',
            'genre': 'Genre',
            'game_photo': 'Game photo',
            'size': 'Size',
            'price': 'Price',
            'description': 'Description'
        }


class GameCreateView(LoginRequiredMixin, CreateView):
    model = Game
    form_class = GameForm
    template_name = 'common/game_form.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class GameEditView(LoginRequiredMixin, UpdateView):
    model = Game
    form_class = GameForm
    template_name = 'common/game_form.html'


class GameDeleteView(LoginRequiredMixin, DeleteView):
    model = Game
    template_name = 'common/game_confirm_delete.html'
    success_url = '/'
