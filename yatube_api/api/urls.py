from django.urls import include, path

from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router_v1 = DefaultRouter()
router_v1.register('posts', PostViewSet)
router_v1.register('groups', GroupViewSet)
router_v1.register(r'posts/(?P<pk_post>[^/.]+)/comments',
                   CommentViewSet, basename='comments')
router_v1.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('', include(router_v1.urls)),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
]
