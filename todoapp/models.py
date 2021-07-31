from django.db import models

class Todo(models.Model):
    todo_item = models.CharField(max_length=80)

    def __str__(self):
        return self.todo_item