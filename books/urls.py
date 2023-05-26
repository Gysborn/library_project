from django.urls import path

from books.views import BookCreateView, BookListView, BookRetrieveView, BookUpdateView, BookDestroyView

urlpatterns = [
    path('create/', BookCreateView.as_view(), name='book_create'),
    path('', BookListView.as_view(), name='book_list'),
    path('<int:pk>/', BookRetrieveView.as_view(), name='book_one'),
    path('update/<int:pk>/', BookUpdateView.as_view(), name='book_update'),
    path('delete/<int:pk>/', BookDestroyView.as_view(), name='book_del'),

]