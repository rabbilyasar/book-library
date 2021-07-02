from django.test import TestCase
from catalog.models import Author
from django.urls import reverse
from django.contrib.auth.models import User
from model_bakery import baker


# class AuthoListViewTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         number_of_authors = 13
#         for author_id in range(number_of_authors):
#             Author.objects.create(first_name=f'John{author_id}',
#                                   last_name=f'Doe{author_id}')

#     def test_view_url_exists_at_desired_location(self):
#         response = self.client.get(reverse(''))


class IndexViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(username='test_user', password='test_password')
        books = baker.make('catalog.Book', _quantity=10)

    def test_view_deny_anonymous(self):
        """Test the view for unauthenticated user if unauthenticated will redirect to login page
        """
        response = self.client.get('/catalog/')
        self.assertRedirects(response, '/login/?next=/catalog/')
        response = self.client.get('/catalog/')
        self.assertRedirects(response, '/login/?next=/catalog/')

    def test_view_url_accesible_by_name(self):
        """Test view is accesible by the reverse method
        """
        self.client.login(username='test_user', password='test_password')
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template_(self):
        """Test view is using correct template
        """
        self.client.login(username='test_user', password='test_password')
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_view_has_context_num_books(self):
        self.client.login(username='test_user', password='test_password')
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('num_books' in response.context)
        self.assertEqual(response.context['num_books'], 10)
