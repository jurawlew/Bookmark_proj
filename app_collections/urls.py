from django.urls import path

from app_collections.views import CreateCollection, DetailCollection, ListCollection

urlpatterns = [
    path('list', ListCollection.as_view(), name='collection_list'),
    path('create', CreateCollection.as_view(), name='collection_create'),
    path('<int:pk>', DetailCollection.as_view(), name='collection_detail'),

]