from rest_framework.routers import DefaultRouter

from django.urls import include, path

from .views import PostViewSet, CommentViewSet, GroupViewSet

# Создаётся роутер
router_v1 = DefaultRouter()
router_v1.register('posts', PostViewSet)
router_v1.register('groups', GroupViewSet)
router_v1.register(r'posts/(?P<pk_post>[^/.]+)/comments',
                   CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(router_v1.urls)),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
]
