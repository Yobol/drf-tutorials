from django.contrib.auth.models import User

from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics
from rest_framework import permissions
from rest_framework import renderers

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

class SnippetHighlightView(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request: Request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view
def api_root(request: Request, format=None):
    """
    First, we're using REST framework's reverse function in order to 
    return fully-qualified URLs; 
    Second, URL patterns are identified by convenience names that
    we will declare later on in our snippets/urls.py.
    """
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets_auth': reverse('snippet-list', request=request, format=format),
    })
