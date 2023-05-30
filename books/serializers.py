from rest_framework import serializers
from books.models import Book
from authors.models import Author
from django.core.exceptions import ValidationError


class BookPagesValidator:
    def __init__(self, total_pages):
        self.total_pages = total_pages

    def __call__(self, value):
        if value < self.total_pages:
            raise ValidationError('Не валидное значение колличества страниц')


class BookSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True, slug_field='last_name', many=True)

    class Meta:
        model = Book
        fields = '__all__'


class BookCreateSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        required=False,
        slug_field='last_name',
        many=True,
        queryset=Author.objects.all()
    )
    pages = serializers.IntegerField(validators=[BookPagesValidator(1)])

    class Meta:
        model = Book
        fields = '__all__'

    def is_valid(self, raise_exception=False):
        self._author = self.initial_data.pop('author')

        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        book = Book.objects.create(**validated_data)

        for author in self._author:
            author_obj = Author.objects.get(id=author)
            book.author.add(author_obj)

        book.save()
        return book


class BookUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id']
