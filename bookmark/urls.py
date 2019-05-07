from django.urls import path
from .views import BookmarkListView, BookmarkCreateView, BookmarkDetailView, BookmarkUdateView, BookmarkDeleteView

urlpatterns = [
    path('', BookmarkListView.as_view(), name='list'),
    path('add/', BookmarkCreateView.as_view(), name='add'),
#    path('detail/', BookmarkDetailView.as_view(), name='detail'),
    path('detail/<int:pk>', BookmarkDetailView.as_view(), name='detail'),
    path('Update/<int:pk>', BookmarkUdateView.as_view(), name='update'),
    path('delete/<int:pk>', BookmarkDeleteView.as_view(), name='delete'),
]
