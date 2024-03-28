from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from tutorials.snippets_drf3 import views

urlpatterns = [
    path('snippets_drf3/', views.SnippetListView2.as_view()),
    path('snippets_drf3/<int:pk>/', views.SnippetDetailView2.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)