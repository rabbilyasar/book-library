from django.test import TestCase
from catalog.forms import AddBookForm


class AddBookFormTests(TestCase):
    def test_title_starting_lowercase(self):
        form = AddBookForm(data={"title": "a lowercase title"})

        self.assertEqual(
            form.errors["title"], ["Should start with an uppercase"]
        )

    def test_title_ending_full_stop(self):
        form = AddBookForm(data={"title": "A stopped title."})
        
        self.assertEqual(
            form.errors["title"], ["Should not end with a full stop"]
        )
    
    def test_title_with_ampersand(self):
        form = AddBookForm(data={"title": ""})
        
        self.assertEqual(
            form.errors["title"], ["This field is required."]
        )