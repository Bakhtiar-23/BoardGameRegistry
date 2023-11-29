# boardgames/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import BoardGame, Gamer, Loan
from .forms import BoardGameForm, LoanForm

@login_required
def boardgame_list(request):
    boardgames = BoardGame.objects.all()
    return render(request, 'boardgames/boardgame_list.html', {'boardgames': boardgames})

@login_required
def boardgame_add(request):
    if request.method == 'POST':
        form = BoardGameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('boardgame_list')
    else:
        form = BoardGameForm()
    return render(request, 'boardgames/boardgame_form.html', {'form': form})

@login_required
def boardgame_edit(request, pk):
    boardgame = get_object_or_404(BoardGame, pk=pk)
    if request.method == 'POST':
        form = BoardGameForm(request.POST, instance=boardgame)
        if form.is_valid():
            form.save()
            return redirect('boardgame_list')
    else:
        form = BoardGameForm(instance=boardgame)
    return render(request, 'boardgames/boardgame_form.html', {'form': form})

@login_required
def boardgame_delete(request, pk):
    boardgame = get_object_or_404(BoardGame, pk=pk)
    boardgame.delete()
    return redirect('boardgame_list')

@login_required
def borrow_game(request, game_id):
    game = get_object_or_404(BoardGame, pk=game_id)
    gamer = Gamer.objects.get(user=request.user)

    # Check if the gamer already has 3 borrowed games
    current_borrowed_games = Loan.objects.filter(borrower=gamer, returned_at__isnull=True).count()

    if current_borrowed_games >= 3:
        return render(request, 'boardgames/borrow_limit_reached.html')

    if request.method == 'POST':
        form = LoanForm(request.POST)
        if form.is_valid():
            loan = form.save(commit=False)
            loan.board_game = game
            loan.borrower = gamer
            loan.save()
            return redirect('boardgames:game_detail', game_id=game_id)
    else:
        form = LoanForm()

    return render(request, 'boardgames/borrow_game.html', {'form': form, 'game': game})