from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Todos(models.Model):
    STATUS_CHOICES = (
        ("OP", "OPEN"),
        ("CL", "CLOSED"),
        ("P", "PENDING")
    )

    title = models.CharField(max_length=300, null=False)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, null=False, default='OP')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # to avoid todos_todos i mean appname_table name we can use this
    # this will create table name what u have mentioned 
    class Meta:
        db_table = "todos"

    def get_todo_edit_url(self):
        # method 1
        # return f"/todos/{self.id}"
        # method 2
        return reverse("todos:edittodo",kwargs={ "id": self.id })

    def get_delete_url(self):
        return reverse("todos:deletetodo", kwargs={ "id": self.id })

    def get_todo_edit_class_url(self):
        return reverse("todos:updatetodo", kwargs={ "pk": self.id })