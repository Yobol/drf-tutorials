from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework import permissions

from tutorials.snippets_auth.models import Snippet
from tutorials.snippets_auth.serializers import SnippetSerializer, UserSerializer
from tutorials.snippets_auth.permissions import IsOwnerOrReadOnly

"""
The create/retrieve/update/delete operations that
we've been using so far are going to be pretty similar
for any model-backed API views we create.
Those bits of common behavior are implemented
in REST framework's mixin classes.
"""

class SnippetListView(
    generics.ListCreateAPIView,
):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def perform_create(self, serializer: SnippetSerializer):
        serializer.save(owner=self.request.user)
        # return super().perform_create(serializer)

class SnippetDetailView(
    generics.RetrieveUpdateDestroyAPIView,
):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer