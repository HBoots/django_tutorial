from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Question, Choice

# GENERIC / CLASS BASED VIEWS
# https://docs.djangoproject.com/en/4.2/topics/class-based-views/


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    # DEFAULT CONTEXT NAME = question_list
    # OVERRIDE DEFAULT TO WHAT IS USED IN TEMPLATE (instead of changing template)
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the most recent 5 published questions."""

        return Question.objects.filter(
            pub_date__lte=timezone.now()).order_by(
            "-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    # DEFAULT CONTEXT NAME = question
    # THIS IS USED IN TEMPLATE SO NO NEED TO OVERRIDE
    template_name = "polls/detail.html"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, pk):
    question = get_object_or_404(Question, pk=pk)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        context = {
            "question": question,
            "error_message": "You did not specify a choice."
        }
        return render(request, "polls/detail.html", context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
