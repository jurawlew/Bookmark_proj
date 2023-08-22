from rest_framework import serializers

from app_bookmarks.models import Bookmark
from app_collections.models import Collection


class ListCollectionSerializers(serializers.ModelSerializer):
    """ """

    class Meta:
        model = Collection
        fields = ['id', 'title']


class CreateCollectionSerializers(serializers.ModelSerializer):
    """ """
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Collection
        fields = ['title', 'description', 'user']

    def create(self, validated_data):
        user = validated_data.pop('user')
        collection = Collection.objects.create(user=user, **validated_data)
        return collection


class BookmarkSerializers(serializers.ModelSerializer):
    """ """

    class Meta:
        model = Bookmark
        fields = ['title']


class CollectionSerializers(serializers.ModelSerializer):
    """ """

    bookmarks = BookmarkSerializers(many=True)

    class Meta:
        model = Collection
        fields = ['title', 'description', 'bookmarks']
