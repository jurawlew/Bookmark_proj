import opengraph_py3

from rest_framework import serializers

from app_bookmarks.models import Bookmark
from app_collections.models import Collection
from app_collections.serializers import CollectionSerializers


class ListBookmarkSerializers(serializers.ModelSerializer):
    """ """
    collections = CollectionSerializers(many=True)

    class Meta:
        model = Bookmark
        fields = ['id', 'title', 'image', 'collections']


class BookmarkSerializers(serializers.ModelSerializer):
    """ """
    collections = CollectionSerializers(many=True)

    class Meta:
        model = Bookmark
        fields = '__all__'

    def update(self, instance, validated_data):
        collections_list = list()
        collections = validated_data.pop('collections', [])
        for i in collections:
            collection = Collection.objects.get(id=i['title'])
            collections_list.append(collection)

        instance.collections.set(collections_list, clear=False)
        instance.save()
        return instance


class CreateBookmarkSerializers(serializers.ModelSerializer):
    """ """
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    type_link = serializers.CharField(required=False)

    class Meta:
        model = Bookmark
        fields = '__all__'

    def create(self, validated_data):
        link = validated_data.get('link')
        user = validated_data.pop('user')

        og = opengraph_py3.OpenGraph(url=link)
        if og.is_valid():
            type_link = og['type']
            image = og['image']
        else:
            type_link = 'website'
            image = None
        bookmark = Bookmark.objects.create(type_link=type_link, image=image, user=user, **validated_data)
        return bookmark
