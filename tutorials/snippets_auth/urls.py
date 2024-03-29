from django.urls import path

from tutorials.snippets_auth import views

snippet_list = views.SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create',
})
snippet_detail = views.SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})
snippet_highlight = views.SnippetViewSet.as_view({
    'get': 'highlight',
})
user_list = views.UserViewSet.as_view({
    'get': 'list',
})
user_detail = views.UserViewSet.as_view({
    'get': 'retrieve',
})

urlpatterns = [
    path('', views.api_root),

    # path('snippets_auth/', views.SnippetListView.as_view(), name='snippet-list'),
    # path('snippets_auth/<int:pk>/', views.SnippetDetailView.as_view(), name='snippet-detail'),
    # path('snippets_auth/<int:pk>/highlight/', views.SnippetHighlightView.as_view(), name='snippet-highlight'),

    # path('users', views.UserListView.as_view(), name='user-list'),
    # path('users/<int:pk>', views.UserDetailView.as_view(), name='user-detail'),

    path('snippets_auth/', snippet_list, name='snippet-list'),
    path('snippets_auth/<int:pk>/', snippet_detail, name='snippet-detail'),
    path('snippets_auth/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),

    path('users', user_list, name='user-list'),
    path('users/<int:pk>', user_detail, name='user-detail'),
]
