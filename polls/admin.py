from django.contrib import admin

# Register your models here.
from .models import Question, Choice, Todo, User

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Todo)
admin.site.register(User)