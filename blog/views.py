# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import Blog


class BlogListView(ListView):
    """
    Insert Doc String Here
    """

    template_name = 'blog/blog.html'
    model = Blog

    def get_short_description(self, articles):
        """
        This function generates a short description for the list view.
        """

        pass

    def get_context_data(self, **kwargs):
        articles = Blog.objects.filter(published_status='Pub').order_by('-date_created')
        context = super(BlogListView, self).get_context_data(**kwargs)
        context['page_title'] = 'jeffreytorres.info'
        context['articles'] = articles
        return context


class BlogDetailView(DetailView):
    """
    Insert Doc String Here
    """

    template_name = 'blog/blog_detail.html'
    model = Blog
