from rest_framework.generics import DestroyAPIView, CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView

from books.models import Book
from books.serializers import BookSerializer, BookCreateSerializer, BookUpdateSerializer, \
    BookDestroySerializer


class BookCreateView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookCreateSerializer


class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookRetrieveView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookUpdateSerializer


class BookDestroyView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDestroySerializer
