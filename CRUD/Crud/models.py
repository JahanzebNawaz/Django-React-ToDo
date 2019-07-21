from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(
        max_length=120,
        help_text='Title of Message'
    )
    message = models.TextField(
        help_text='What is in mind ....'
    )

    def __str__(self):
        return self.title
