from django.db import models

from authors.models import Author


class Book(models.Model):
    title = models.CharField(max_length=150, blank=True)
    description = models.TextField(max_length=2000, blank=True)
    pages = models.PositiveIntegerField(blank=True)
    total = models.PositiveIntegerField(blank=True)
    author = models.ManyToManyField(Author, blank=True)
    created = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Дата последнего обновления", auto_now=True)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title

