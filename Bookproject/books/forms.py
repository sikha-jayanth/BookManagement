from django import forms
from books.models import Book
from django.forms import ModelForm


# class BookCreateForms(forms.Form):
#     book_name = forms.CharField(max_length=100)
#     author = forms.CharField(max_length=100)
#     price = forms.IntegerField()
#     pages = forms.IntegerField()


class BookCreateForms(ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        bookname = cleaned_data.get('book_name')
        bookprice = cleaned_data.get('price')
        bookpages = cleaned_data.get('pages')
        book = Book.objects.filter(book_name=bookname)

        if book:
            msg = "Book with same name already exists"
            self.add_error('book_name', msg)
        if bookprice < 100:
            msg = "Enter price greater than 100"
            self.add_error('price', msg)
        if bookpages < 50:
            msg = "Page number should be greater than 50"
            self.add_error('pages', msg)


class BookpUpdateForm(ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
