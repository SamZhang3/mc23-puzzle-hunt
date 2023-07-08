from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from puzzlehunt_app.models import Puzzle

# Create your views here.

def index(request):
    puzzles = Puzzle.objects.order_by("id")
    context = {"puzzles": puzzles}
    return render(request, "puzzlehunt_app/index.html", context)

@ensure_csrf_cookie
def puzzle(request, puzzle_id):
    puzzle = get_object_or_404(Puzzle, pk=puzzle_id)
    context = {"puzzle": puzzle}
    return render(request, "puzzlehunt_app/puzzle.html", context)

def answer_filter(answer):
    return "".join([c for c in answer if not c.isspace()]).lower()

def submit(request, puzzle_id, submission):
    puzzle = get_object_or_404(Puzzle, pk=puzzle_id)
    submitted = answer_filter(submission)
    correct = answer_filter(puzzle.answer)
    if submitted == correct:
        return HttpResponse("Correct!")
    else:
        return HttpResponse(submission.upper() + " is incorrect.")
