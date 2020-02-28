from django.shortcuts import render, get_object_or_404, redirect

from django.urls import reverse

from django.views.generic import (
	DetailView,
	ListView,
	UpdateView,
	CreateView,
	DeleteView
)

from .forms import ArticleModelForm

from .models import Article

from django.contrib.auth import authenticate, login, logout

from django.conf import settings

from django.contrib.auth.decorators import login_required

# @login_required
class ArticleCreateView(CreateView):
	template_name = 'blog/article_create.html'
	form_class = ArticleModelForm
	queryset = Article.objects.all()

class ArticleListView(ListView):
	template_name = 'blog/article_list.html'
	queryset = Article.objects.all()

class ArticleDetailView(DetailView):
	template_name = 'blog/article_detail.html'

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Article, id=id_)

class ArticleUpdateView(UpdateView):
	template_name = 'blog/article_create.html'
	form_class = ArticleModelForm

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Article, id=id_)

	def form_valid(self, form):
		return super().form_valid(form)

class ArticleDeleteView(DeleteView):
	template_name = 'blog/article_delete.html'

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Article, id=id_)

	def get_success_url(self):
		return reverse('articles:article-list')