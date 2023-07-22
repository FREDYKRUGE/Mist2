from django.shortcuts import render

from Mist2.games.models import Game


def home_page(request):
    games = Game.objects.all()

    context = {
        'games': games
    }
    return render(request, 'common/home.html', context=context)
