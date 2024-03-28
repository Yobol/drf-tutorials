from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from tutorials.snippets_drf2 import views

urlpatterns = [
    path('snippets_drf2/', views.SnippetListView.as_view()),
    path('snippets_drf2/<int:pk>/', views.SnippetDetailView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)