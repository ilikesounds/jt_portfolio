# from django.shortcuts import render
from django.views.generic.list import ListView
from blog.models import Blog


class BlogListView(ListView):
    """
    Insert Doc String Here
    """

    template_name = 'blog/home.html'
    model = Blog

    def get_context_data(self, **kwargs):
        articles = Blog.objects.filter(published_status='Pub').order_by('-date_created')
        context = super(BlogListView, self).get_context_data(**kwargs)
        context['page_title'] = 'jeffreytorres.info'
        context['articles'] = articles
        return context

        
