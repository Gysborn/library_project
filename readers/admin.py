from django.contrib import admin
from django.core.exceptions import ValidationError

from readers.forms import ReaderForm
from readers.models import Reader


class ReaderAdmin(admin.ModelAdmin):
    form = ReaderForm


admin.register(Reader, ReaderAdmin)

admin.site.register(Reader, ReaderAdmin)
