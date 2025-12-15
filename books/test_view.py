from django.test import TestCase
from django.urls import reverse
from .models import Book

class BookModelTests(TestCase):

    def setUp(self):
        # Create a sample book record for testing
        self.book = Book.objects.create(
            name="Test Book",
            author_name="Test Author",
            price=9.99,
            genre="cl",
            book_type="hc"
        )
        
    def test_get_absolute_url(self):
        book = Book.objects.get(id=1)
        expected_url = reverse('books:detail', kwargs={'pk': book.pk})
        self.assertEqual(book.get_absolute_url(), expected_url)