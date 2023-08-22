from django.urls import path

from app_bookmarks.views import ListBookmark, CreateBookmark, DetailBookmark

urlpatterns = [
    path('list', ListBookmark.as_view(), name='bookmark_list'),
    path('create', CreateBookmark.as_view(), name='bookmark_create'),
    path('<int:pk>', DetailBookmark.as_view(), name='bookmark_detail'),
]
