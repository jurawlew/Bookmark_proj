from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from app_collections.models import Collection
from app_collections.serializers import ListCollectionSerializers, CreateCollectionSerializers, \
    CollectionSerializers
from app_users.permissions import IsOwnerPermissions


class ListCollection(generics.ListAPIView):
    """ """
    queryset = Collection.objects.all()
    serializer_class = ListCollectionSerializers
    permission_classes = (IsAuthenticated, IsOwnerPermissions,)
    http_method_names = ['get']


class CreateCollection(generics.CreateAPIView):
    """ """
    serializer_class = CreateCollectionSerializers
    permission_classes = (IsAuthenticated,)
    http_method_names = ['post']


class DetailCollection(generics.RetrieveUpdateDestroyAPIView):
    """ """
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializers
    permission_classes = (IsAuthenticated, IsOwnerPermissions,)
    http_method_names = ['get', 'put', 'patch', 'delete']
