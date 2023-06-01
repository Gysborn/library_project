from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from library_project import settings
from authors.views import AuthorViewSet, AuthorUpdateCreateViewSet

router_author = routers.SimpleRouter()
router_author.register('author', AuthorViewSet)

router = routers.SimpleRouter()
router.register('create', AuthorUpdateCreateViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('readers/', include(('readers.urls', 'readers'))),
    path('books/', include(('books.urls', 'books'))),
]

urlpatterns += router.urls
urlpatterns += router_author.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

