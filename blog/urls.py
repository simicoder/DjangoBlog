from django.urls import path
from .views import (
	ArticleDetailView,
	ArticleListView,
	ArticleCreateView,
	ArticleUpdateView,
	ArticleDeleteView
)


app_name = 'articles'
urlpatterns = [
	path('posts', ArticleListView.as_view(), name='article-list'),
	path('posts/<int:id>/', ArticleDetailView.as_view(), name='article-detail'),
	path('posts/<int:id>/update', ArticleUpdateView.as_view(), name='article-update'),
	path('posts/<int:id>/delete', ArticleDeleteView.as_view(), name='article-delete'),
	path('', ArticleCreateView.as_view(), name='article-create')
]