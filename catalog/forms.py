from django import forms
from .models import Book


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title"]

    def clean_title(self):
        title = self.cleaned_data['title']
        if not title:
            return title
        if not title[0].isupper():
            self.add_error("title", "Should start with an uppercase")
        if title.endswith("."):
            self.add_error("title", "Should not end with a full stop")

        return title
