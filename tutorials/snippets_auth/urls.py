from django.urls import path

from tutorials.snippets_auth import views

urlpatterns = [
    path('snippets_auth/', views.SnippetListView.as_view()),
    path('snippets_auth/<int:pk>/', views.SnippetDetailView.as_view()),

    path('users', views.UserListView.as_view()),
    path('users/<int:pk>', views.UserDetailView.as_view()),
]
