from rest_framework import mixins
from rest_framework import generics
from rest_framework.request import Request

from tutorials.snippets.models import Snippet
from tutorials.snippets.serializers import SnippetSerializer


"""
The create/retrieve/update/delete operations that
we've been using so far are going to be pretty similar
for any model-backed API views we create.
Those bits of common behavior are implemented
in REST framework's mixin classes.
"""

class SnippetListView(
    generics.GenericAPIView,
    mixins.ListModelMixin, mixins.CreateModelMixin,
):
    """
    We're building our view using GenericAPIView,
    and adding in ListModelMixin and CreateModelMixin.

    The base class provides the core functionality,
    and the mixin classes provide the .list() and .create() actions.
    We're then explicitly binding the get and post methods to the appropriate actions. 
    Simple enough stuff so far.
    
    List all code snippets, or create a new snippet.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class SnippetListView2(
    generics.ListCreateAPIView,
):
    """
    Equal to SnippetListView.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class SnippetDetailView(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin
):
    """
    We're using the GenericAPIView class to provide the core functionality,
    and adding in mixins to provide the .retrieve(), .update() and .destroy() actions.

    Retrieve, update or delete a code snippet.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request: Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def post(self, request: Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request: Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class SnippetDetailView2(
    generics.RetrieveUpdateDestroyAPIView,
):
    """
    Equal to SnippetDetailView.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
