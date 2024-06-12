from django.db import models
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower

class Genre(models.Model):
    name = models.CharField(
        max_length=200,
        unique=True,
        help_text = "Enter a book genre"
    )

# Create your models here.
# book
# book instance
# genre
# writer


