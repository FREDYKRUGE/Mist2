from django.shortcuts import render, redirect

from Mist2.common.forms import SearchForm
from Mist2.games.models import Game


def home_page(request):
    games = Game.objects.all()
    search_form = SearchForm()
    search_results = None

    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            games = games.filter(name__icontains=search_form.cleaned_data['game_name'])
    context = {
        'games': games,
        'search_form': search_form,
        'search_results': search_results,
    }
    return render(request, 'common/home.html', context=context)
