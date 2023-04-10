import datetime
from django.db import models
from django.utils import timezone

# NOTES ON MODELS
# Optional first param in field is readable name for the field. e.g "date published".
# ** BEST PRACTICE: Create UUID ids for primary keys (import uuid. configure field) Django will default to integers.
# ** CHANGING A PRIMARY KEY:

# NOTES ON MIGRATIONS
# View the SQL commands that will be sent to database
# $ python manage.py sqlmigrate polls 0001


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
