from django.urls import path

from tutorials.snippets_auth import views

urlpatterns = [
    path('', views.api_root),

    path('snippets_auth/', views.SnippetListView.as_view(), name='snippet-list'),
    path('snippets_auth/<int:pk>/', views.SnippetDetailView.as_view(), name='snippet-detail'),
    path('snippets_auth/<int:pk>/highlight/', views.SnippetHighlightView.as_view(), name='snippet-highlight'),

    path('users', views.UserListView.as_view(), name='user-list'),
    path('users/<int:pk>', views.UserDetailView.as_view(), name='user-detail'),
]
