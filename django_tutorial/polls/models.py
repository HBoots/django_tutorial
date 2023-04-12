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

# NOTES ON RELATED OBJECT REF:
# https://docs.djangoproject.com/en/4.2/ref/models/relations/
# Related object reference methods are available on a the 'object_set' of a Foreign Key (OneToMany) or ManyToMany relation object.
# e.g
# Related object ref methods operate on 'choice_set' which is a property of Question.
# question.choice_set.create(...)


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
