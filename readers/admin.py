from django.contrib import admin
from django.core.exceptions import ValidationError
from django.shortcuts import redirect

from books.models import Book
from readers.models import Reader


@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'created', 'updated')
    list_filter = ('status',)
    actions = ('delete_readers_books', 'change_reader_status',)

    def save_model(self, request, obj, form, change):
        books = form.cleaned_data['books']
        if len(books) > 3:
            raise ValidationError(
                'Вы не можете взять более 3-х книг'
            )
        phone = str(form.cleaned_data['phone_number'])
        if not phone.startswith('+7'):
            raise ValidationError('Номер телефона должен начинаться с +7')
        if len(phone) != 12 or not phone[1:].isdigit():
            raise ValidationError('Номер телефона должен состоять из 11 цифр')

        for book in books:
            book_obj = Book.objects.get(title=book)
            if book_obj.total == 0:
                raise ValidationError(f'{book_obj.title} нет в наличии')
            book_obj.total -= 1
            book_obj.save()

        super().save_model(request, obj, form, change)

    def delete_readers_books(self, request, objs):
        for reader in objs:
            lib = reader.books.all()
            for li in lib:
                book = Book.objects.get(title=li)
                book.total += 1
                book.save()

            reader.books.set([])


    def change_reader_status(self, request, objs):
        for reader in objs:
            if reader.status:
                reader.status = False
            else:
                reader.status = True

            reader.save()
