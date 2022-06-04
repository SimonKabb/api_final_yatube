from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404

from rest_framework import filters, permissions, viewsets
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Follow, Group, Post
from api.serializers import (CommentSerializer, FollowSerializer,
                             GroupSerializer, PostSerializer)


class CreatUpdateDestroyViewSet(viewsets.ModelViewSet):
    """Материнский класс включающий методы для проверки автора контента
    и пагинацию"""
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента невозможно')
        super(CreatUpdateDestroyViewSet, self).perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied('Удаление чужого контента невозможно')
        super(CreatUpdateDestroyViewSet, self).perform_destroy(instance)


class PostViewSet(CreatUpdateDestroyViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(CreatUpdateDestroyViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs.get("pk_post")
        post = get_object_or_404(Post, id=post_id)
        return post.comments.all()


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class FollowViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)
