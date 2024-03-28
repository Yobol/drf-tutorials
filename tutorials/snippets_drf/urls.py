from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from tutorials.snippets_drf import views

urlpatterns = [
    path('snippets_drf/', views.snippet_list),
    path('snippets_drf/<int:pk>/', views.snippet_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)