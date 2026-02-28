from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import Article

class HomePageView(ListView):
    model = Article
    template_name = 'news/home.html'
    context_object_name = 'articles'
    paginate_by = 10
    def get_queryset(self):
        qs = super().get_queryset()
        title_filter = self.request.GET.get('title', None)
        if title_filter:
            qs = qs.filter(title__icontains=title_filter)
        return qs.order_by('-created_at')

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'news/detail.html'
    context_object_name = 'article'
   
    from django.views.generic import ListView, DetailView
from .models import Article
from django.db.models import Q

class NewsListView(ListView):
    model = Article
    template_name = 'news/home.html'
    context_object_name = 'articles'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset().filter(is_published=True)
        search_query = self.request.GET.get('q', '')
        if search_query:
            queryset = queryset.filter(title__icontains=search_query)
        return queryset.order_by('-created_at')

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'news/article_detail.html'
    context_object_name = 'article'
# Create your views here.
