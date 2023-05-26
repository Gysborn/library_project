from rest_framework.viewsets import ModelViewSet

from authors.models import Author
from authors.serializers import AuthorSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
