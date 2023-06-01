from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import DestroyAPIView, CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView
from readers.models import Reader
from readers.permissions import IsOwnerOrAdmin
from readers.serializers import ReaderSerializer, ReaderCreateSerializer, ReaderUpdateSerializer, \
    ReaderDestroySerializer


class ReaderCreateView(CreateAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderCreateSerializer


class ReaderListView(ListAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer
    permission_classes = [IsAdminUser]


class ReaderRetrieveView(RetrieveAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer
    permission_classes = [IsOwnerOrAdmin]


class ReaderUpdateView(UpdateAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderUpdateSerializer
    permission_classes = [IsOwnerOrAdmin]


class ReaderDestroyView(DestroyAPIView):
    queryset = Reader.objects.all()
    serializer_class = ReaderDestroySerializer
    permission_classes = [IsOwnerOrAdmin]
