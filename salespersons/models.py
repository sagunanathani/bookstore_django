from django.db import models
from django.contrib.auth.models import User

class Salesperson(models.Model):
    # Each salesperson is linked to one unique User account
    username = models.OneToOneField(User, on_delete=models.CASCADE)

    # Salesperson's name
    name = models.CharField(max_length=120)

    # Bio with a default value
    bio = models.TextField(default="no bio...")

    # Picture field (optional, will be used later in views/templates)
    pic = models.ImageField(upload_to="salesperson_pics/", blank=True, null=True, help_text="Upload salesperson photo")

    def __str__(self):
        return f"{self.name} ({self.username})"