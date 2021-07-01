from django.test import TestCase
from catalog.models import Book, Genre, BookInstance, Author
from django.urls import reverse


class TestModels(TestCase):
    @classmethod
    def setUpTestData(self):
        thriller = Genre.objects.create(name='thriller')
        scifi = Genre.objects.create(name='scifi')
        book = Book.objects.create(
            title='test title',
            summary='test summary',
            isbn='test isbn',
        )
        book.genre.set([thriller.pk, scifi.pk])

    def test_book_has_genre(self):
        """checks for genres in book
        """
        book = Book.objects.first()
        self.assertEqual(book.genre.count(), 2)

    def test_book_str(self):
        """Checks str for book
        """
        book = Book.objects.first()
        self.assertEqual(str(book), "test title")

    def test_book_absolute_url_with_200(self):
        book = Book.objects.first()
        response = self.client.get(book.get_absolute_url())
        self.assertEqual(response.status_code, 200)

    def test_genre_str(self):
        genre = Genre.objects.first()
        self.assertEqual(str(genre), "thriller")
