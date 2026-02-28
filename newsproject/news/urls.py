from django.urls import path
from .views import HomePageView, ArticleDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
]
from django.shortcuts import render

def home(request):
    return render(request, 'news/home.html') 
from django.urls import path
from .views import NewsListView, ArticleDetailView

urlpatterns = [
    path('', NewsListView.as_view(), name='news-list'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
] # создадите шаблон позже