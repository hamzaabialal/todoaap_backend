from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class ToDoModel(models.Model):
    title = models.CharField(max_length=30)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

        # Check for a name (letters and spaces only)
