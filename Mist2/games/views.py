from django import forms
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
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
    template_name = 'games/game_form.html'
    success_url = '/'

    def form_valid(self, form):
        game = form.save(commit=False)
        game.user = self.request.user  # Set the currently logged-in user as the creator
        game.save()
        return super().form_valid(form)


class GameEditView(LoginRequiredMixin, UpdateView):
    model = Game
    form_class = GameForm
    template_name = 'games/game_form.html'


class GameDeleteView(LoginRequiredMixin, DeleteView):
    model = Game
    template_name = 'games/game_confirm_delete.html'
    success_url = '/'


class GameDetailsView(DetailView):
    model = Game
    template_name = 'games/game_details.html'
    context_object_name = 'game'
    pk_url_kwarg = 'pk'
