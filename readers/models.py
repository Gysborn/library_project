from django.db import models

from books.models import Book


class Reader(models.Model):
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    phone_number = models.CharField(max_length=12, unique=True, blank=True)
    status = models.BooleanField(default=True)
    books = models.ManyToManyField(Book, blank=True)
    created = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Дата последнего обновления", auto_now=True)

    class Meta:
        verbose_name = 'Читатель'
        verbose_name_plural = 'Читатели'

    # def __str__(self):
    #     return self.last_name




