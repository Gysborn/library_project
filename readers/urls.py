from django.urls import path

from readers.views import ReaderCreateView, ReaderListView, ReaderRetrieveView, ReaderUpdateView, ReaderDestroyView

urlpatterns = [
    path('create/', ReaderCreateView.as_view(), name='reader_create'),
    path('', ReaderListView.as_view(), name='reader_list'),
    path('<int:pk>/', ReaderRetrieveView.as_view(), name='reader_one'),
    path('update/<int:pk>/', ReaderUpdateView.as_view(), name='reader_update'),
    path('delete/<int:pk>/', ReaderDestroyView.as_view(), name='reader_del'),

]