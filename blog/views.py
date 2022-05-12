from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from django.views.generic import(
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)

from .models import Article
from .forms import ArticleForm

# Create your views here.


class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all()

class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'
    queryset = Article.objects.all()

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Article, id=id)

class ArticleLCreateView(CreateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleForm
    queryset = Article.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)

class ArticleUpdateView(UpdateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleForm
    queryset = Article.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Article, id=id)

class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'
    queryset = Article.objects.all()

    def get_object(self):
        id = self.kwargs.get("id")
        return get_object_or_404(Article, id=id)

    def get_success_url(self) -> str:
        return reverse('articles:article-list')