# TODO:  Напишите свой вариант
from posts.models import Comment, Post, Group
from rest_framework import viewsets
from django.core.exceptions import PermissionDenied
from .serializers import CommentSerializer, PostSerializer, GroupSerializer
from django.shortcuts import get_object_or_404


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        post_id = self.kwargs.get("pk_post")
        post = get_object_or_404(Post, id=post_id)
        return post.comments.all()

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента невозможно')
        super(CommentViewSet, self).perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied('Удаление чужого контента невозможно')
        super(CommentViewSet, self).perform_destroy(instance)
