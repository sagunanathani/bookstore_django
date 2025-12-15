
from django.db import models

# Create models here.
class Customer(models.Model):
    # Customer's name
    name = models.CharField(max_length=120, help_text="Customer's name")

    # Notes with a default value
    notes = models.TextField(default="no notes...", help_text="Any notes the customer wants to make")

    # Picture field (optional, will be used later in views/templates)
    pic = models.ImageField(upload_to="customer_pics/", blank=True, null=True, help_text="Upload customer photo")

    def __str__(self):
        return str(self.name)