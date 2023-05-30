from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from books.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created', 'updated', 'customer_link',)
    actions = ('set_quantity_zero',)

    def customer_link(self, obj):
        cust = obj.author.first()
        url = reverse("admin:authors_author_changelist") + str(cust.pk)
        return format_html(f'<a href="{url}">{cust}</a>')

    customer_link.short_description = 'Авторы'

    def set_quantity_zero(self, request, objs):
        for book in objs:
            book.total = 0
            book.save()
