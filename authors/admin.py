from django.contrib import admin

from authors.models import Author


# admin.site.register(Author)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'created', 'updated', 'photo',)
