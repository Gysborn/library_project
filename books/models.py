from django.db import models

from authors.models import Author


class Book(models.Model):
    title = models.CharField(max_length=150, blank=True)
    description = models.CharField(max_length=2000, blank=True)
    pages = models.SmallIntegerField()
    total = models.SmallIntegerField()
    author = models.ManyToManyField(Author)
    created = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Дата последнего обновления", auto_now=True)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.title

