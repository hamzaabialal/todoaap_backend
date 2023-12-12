from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class ToDoModel(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def clean(self):
        super().clean()

        # Check for a name (letters and spaces only)
        if not all(char.isalpha() or char.isspace() for char in self.title):
            raise ValidationError('Title should contain only letters and spaces (for names).')

        # Check for a username (alphanumeric and no dots)
        if not self.title.replace('_', '').isalnum():
            raise ValidationError('Title should be alphanumeric (for usernames) and should not contain dots.')

        # Check for an email (contain "@" and ".")
        if '@' not in self.title or '.' not in self.title:
            raise ValidationError('Title should contain "@" and "." (for emails).')