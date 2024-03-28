from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser

from tutorials.snippets.models import Snippet
from tutorials.snippets.serializers import SnippetSerializer


@csrf_exempt
def snippet_list(request: HttpRequest):
    """
    Note that because we want to be able to POST to this view from clients
    that won't have a CSRF token we need to mark the view as csrf_exempt.
    This isn't something that you'd normally want to do, 
    and REST framework views actually use more sensible behavior than this, 
    but it'll do for our purposes right now.

    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, status=200, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def snippet_detail(request: HttpRequest, pk: int):
    """
    Note that because we want to be able to POST to this view from clients
    that won't have a CSRF token we need to mark the view as csrf_exempt.
    This isn't something that you'd normally want to do, 
    and REST framework views actually use more sensible behavior than this, 
    but it'll do for our purposes right now.

    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data, status=200)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)

