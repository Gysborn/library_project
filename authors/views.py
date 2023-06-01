from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAdminUser
from authors.models import Author
from authors.serializers import AuthorSerializer
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin


class AuthorViewSet(ListModelMixin, GenericViewSet, RetrieveModelMixin):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorUpdateCreateViewSet(CreateModelMixin, GenericViewSet, UpdateModelMixin):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminUser]

