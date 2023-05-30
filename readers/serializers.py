from rest_framework import serializers
from django.core.exceptions import ValidationError
from books.models import Book
from readers.models import Reader


class ReaderSerializer(serializers.ModelSerializer):
    books = serializers.SlugRelatedField(read_only=True, slug_field='title', many=True)

    class Meta:
        model = Reader
        fields = '__all__'


class ReaderCreateSerializer(serializers.ModelSerializer):
    books = serializers.SlugRelatedField(
        required=False,
        slug_field='title',
        many=True,
        queryset=Book.objects.all()
    )

    def validate(self, attrs):
        phone = str(attrs.get('phone_number'))
        if not phone.startswith('+7'):
            raise ValidationError('Номер телефона должен начинаться с +7')
        if len(phone) != 12 or not phone[1:].isdigit():
            raise ValidationError('Номер телефона должен состоять из 11 цифр')

        return super().validate(attrs)

    class Meta:
        model = Reader
        fields = '__all__'

    def is_valid(self, raise_exception=False):
        self._books = self.initial_data.pop('books')

        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        if len(self._books) > 3:
            raise ValidationError('Вы не можете взять более 3-х книг')
        reader = Reader.objects.create(**validated_data)

        for book in self._books:
            book_obj = Book.objects.get(id=book)
            if book_obj.total < 1:
                raise ValidationError(f'{book_obj.title} нет в наличии')
            reader.books.add(book_obj)
            book_obj.total -= 1
            book_obj.save()

        reader.save()
        return reader


class ReaderUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = '__all__'

    def update(self, instance, validated_data):
        self._books = self.initial_data.pop('books')
        if len(self._books) > 3:
            raise ValidationError('Вы не можете взять более 3-х книг')

        for book in self._books:
            book_obj = Book.objects.get(id=book)
            if book_obj.total < 1:
                raise ValidationError(f'{book_obj.title} нет в наличии')
            book_obj.total -= 1
            book_obj.save()

        return super().update(instance, validated_data)


class ReaderDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reader
        fields = ['id']
