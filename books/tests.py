from django.test import TestCase
from .models import Book
# Create your tests here.
class BookModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Book.objects.create(
        name='Pride and Prejudice',
        author_name='Jane Austen',
        genre='classic',
        book_type='hardcover',
        price=23.71,
        notes="Famous romantic novel"   
    )

    def test_book_name_label(self):
        # Get a book object to test
        book = Book.objects.get(id=1)
        # Get the metadata for the 'name' field
        field_label = book._meta.get_field('name').verbose_name
        # Compare the value to the expected result
        self.assertEqual(field_label, 'name')

    def test_author_name_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('author_name').max_length
        self.assertEqual(max_length, 120)

    def test_price_help_text(self):
        book = Book.objects.get(id=1)
        help_text = book._meta.get_field('price').help_text
        self.assertEqual(help_text, 'in US dollars $')

    def test_object_name_is_book_name(self):
        book = Book.objects.get(id=1)
        expected_object_name = book.name
        self.assertEqual(str(book), expected_object_name)