import datetime
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from .models import Question


class QuestionModelTests(TestCase):
    def test_was_published_recently_future(self):
        """.was_published_recently() returns False for a pub_date in the future."""

        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)

        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_too_old(self):
        """.was_published_recently() returns False for a pub_date more than 1 day ago."""
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_recent(self):
        """.was_published_recently() returns True for a pub_date less than 1 day ago."""
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """If no questions exist, display appropriate message."""
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])

    def test_past_question(self):
        """Question with a pub_date in the past are displayed on index page."""
        question = create_question(question_text="Past question", days=-30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(
            response.context["latest_question_list"], [question])

    def test_future_question(self):
        """Questions with a pub_date in the future are NOT displayed on the index page."""
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])

    def test_future_and_past_question(self):
        """If both future and past questions exist, only past questions are displayed on the index page."""
        question = create_question(question_text="Past question", days=-30)
        create_question(question_text="Future question", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(
            response.context["latest_question_list"], [question])

    def test_two_past_questions(self):
        """The questions index page can display mulitple questions."""
        question1 = create_question(question_text="Past question 1", days=-30)
        question2 = create_question(question_text="Past question 2", days=-5)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"], [
                                 question2, question1])


class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """Future question queries return 404 in Detail View"""
        future_question = create_question(
            question_text="Future question.", days=5)
        url = reverse("polls:detail", args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """Past question queries return 202 and the text is displayed in the Detail View."""
        past_question = create_question(question_text="Past question", days=-5)
        response = self.client.get(
            reverse("polls:detail", args=(past_question.id,)))
        self.assertContains(response, past_question.question_text)


def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)
