from rest_framework.generics import DestroyAPIView, CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView

from readers.models import Reader
from readers.serializers import ReaderSerializer, ReaderCreateSerializer, ReaderUpdateSerializer, \
    ReaderDestroySerializer


class ReaderCreateView(CreateAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderCreateSerializer


class ReaderListView(ListAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer


class ReaderRetrieveView(RetrieveAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer


class ReaderUpdateView(UpdateAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderUpdateSerializer


class ReaderDestroyView(DestroyAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderDestroySerializer
