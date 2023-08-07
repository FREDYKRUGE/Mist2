from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from Mist2.common.forms import SearchForm, CommentForm
from Mist2.common.models import Like
from Mist2.games.models import Game

UserModel = get_user_model()


def home_page(request):
    user = UserModel
    games = Game.objects.all()
    search_form = SearchForm()
    search_results = None

    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            games = games.filter(name__icontains=search_form.cleaned_data['game_name'])
    context = {
        'user': user,
        'games': games,
        'search_form': search_form,
        'search_results': search_results,
    }
    return render(request, 'common/home.html', context=context)


class AddToLibraryView(LoginRequiredMixin, View):
    def get(self, request, pk):
        game = get_object_or_404(Game, pk=pk)
        request.user.library.add(game)  # Add the game to the user's library
        return redirect('details_game', pk=pk)  # Redirect back to the game's details page


def library_view(request):
    user = request.user
    if user.is_authenticated:
        library_games = user.library.all()  # Retrieve games from the user's library
        return render(request, 'common/library.html', {'games': library_games})
    return render(request, 'common/library.html')  # Render an empty library for non-authenticated users


def remove_from_library(request, pk):
    if request.user.is_authenticated:
        try:
            game = Game.objects.get(pk=pk)
            request.user.library.remove(game)
        except Game.DoesNotExist:
            pass
    return redirect('library')


@login_required(login_url='/accounts/login')
def like_functionality(request, game_id):
    game = Game.objects.get(pk=game_id)
    like = Like.objects.filter(to_game_id=game_id, user=request.user).first()

    if like:
        like.delete()
    else:
        like = Like(to_game=game, user=request.user)
        like.save()

    return redirect(request.META['HTTP_REFERER'] + f'#{game_id}')


@login_required(login_url='/accounts/login')
def add_comment(request, game_id):
    if request.method == 'POST':
        game = Game.objects.get(id=game_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.to_game = game
            comment.user = request.user
            comment.save()
        return redirect(request.META['HTTP_REFERER'] + f"#{game_id}")
