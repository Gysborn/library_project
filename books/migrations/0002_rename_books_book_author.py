# Generated by Django 4.2.1 on 2023-05-17 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='books',
            new_name='author',
        ),
    ]
