from django import forms
from django.core.exceptions import ValidationError

from books.models import Book
from readers.models import Reader


class ReaderForm(forms.ModelForm):
    class Meta:
        model = Reader
        fields = ['first_name', 'last_name', 'phone_number', 'status', 'books']

    def clean_books(self):
        books = self.cleaned_data.get('books')
        qs = Book.objects.all()
        for b in books:
            res = qs.get(title=b)
            if res.total == 0:
                raise ValidationError(f'{b}: в наличии нет ни одного экземпляра')
            res.total -= 1
            res.save()

        if books.count() > 3:
            raise ValidationError('Вы не можете взять более 3-х книг')

        return books
