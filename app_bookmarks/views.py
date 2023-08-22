from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from app_bookmarks.models import Bookmark
from app_bookmarks.serializers import ListBookmarkSerializers, CreateBookmarkSerializers, \
    BookmarkSerializers
from app_users.permissions import IsOwnerPermissions


class ListBookmark(generics.ListAPIView):
    """ """
    queryset = Bookmark.objects.all()
    serializer_class = ListBookmarkSerializers
    permission_classes = (IsOwnerPermissions,)
    http_method_names = ['get']


class CreateBookmark(generics.CreateAPIView):
    """ """
    serializer_class = CreateBookmarkSerializers
    permission_classes = (IsAuthenticated,)
    http_method_names = ['post']


class DetailBookmark(generics.RetrieveUpdateDestroyAPIView):
    """ """
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializers
    permission_classes = (IsAuthenticated, IsOwnerPermissions,)
    http_method_names = ['get', 'put', 'patch', 'delete']
