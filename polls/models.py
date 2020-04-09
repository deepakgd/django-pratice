import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=300)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class User(models.Model):
    name = models.CharField(max_length=150, null=False)
    age = models.IntegerField(null=True)
    email = models.EmailField(null=False, unique=True)
    mobile = models.CharField(max_length=10)

class Todo(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=1000)
    status = models.CharField(max_length=20)
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)