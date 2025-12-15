from django.db import models
from books.models import Book   # Import Book model from the same app

class Sale(models.Model):
    # Foreign key to Book
    book = models.ForeignKey(Book, on_delete=models.CASCADE, help_text="Book being sold")

    # Quantity of books sold
    quantity = models.PositiveIntegerField(help_text="Number of books sold in this transaction")

    # Total sale price (entered manually for simplicity)
    price = models.FloatField(help_text="Total sale price (e.g., book price * quantity)")

    # Date of sale (auto-generated)
    date_created = models.DateTimeField(auto_now_add=True, help_text="Date of sale (auto-set)")

    def __str__(self):
        return f"Sale of {self.quantity} x {self.book.name} on {self.date_create.strftime('%Y-%m-%d')}"
    

