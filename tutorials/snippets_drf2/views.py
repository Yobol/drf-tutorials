from django.http import Http404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from tutorials.snippets.models import Snippet
from tutorials.snippets.serializers import SnippetSerializer


"""
# Request objects

REST framework introduces a Request object that extends the regular HttpRequest,
and provides more flexible request parsing.
The core functionality of the Request object is the request.data attribute,
which is similar to request.POST, but more useful for working with Web APIs.


# Response objects

REST framework also introduces a Response object,
which is a type of TemplateResponse that takes
unrendered content and uses content negotiation to
determine the correct content type to return to the client.


# Status codes

Using numeric HTTP status codes in your views doesn't always make for obvious reading,
and it's easy to not notice if you get an error code wrong.
REST framework provides more explicit identifiers for each status code,
such as HTTP_400_BAD_REQUEST in the status module. 
It's a good idea to use these throughout rather than using numeric identifiers.


# Wrapping API views

REST framework provides two wrappers you can use to write API views.

The @api_view decorator for working with function based views.
The APIView class for working with class-based views.
These wrappers provide a few bits of functionality such as 
making sure you receive Request instances in your view, 
and adding context to Response objects so that content negotiation can be performed.

The wrappers also provide behavior such as returning 405 Method Not Allowed responses when appropriate, and handling any ParseError exceptions that occur when accessing request.data with malformed input.
"""

class SnippetListView(APIView):
    """
    To take advantage of the fact that our responses are 
    no longer hardwired to a single content type 
    let's add support for format suffixes to our API endpoints. 
    Using format suffixes gives us URLs that explicitly refer to a given format,
    and means our API will be able to handle URLs such as http://example.com/snippets_drf.json.

    List all code snippets, or create a new snippet.
    """
    def get(self, request: Request, format: str = None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SnippetDetailView(APIView):
    """
    Retrieve, update or delete a code snippet.
    """
    def get_object(self, pk: int) -> Snippet:
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request: Request, pk: int, format: str = None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request: Request, pk: int, format: str = None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk: int, format: str = None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
