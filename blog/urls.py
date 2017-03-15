from django.conf.urls import url
from .views import BlogListView, BlogDetailView

urlpatterns = [
    url(r'^$',
        BlogListView.as_view(),
        name='blog'),
    url(r'^detail/(?P<slug>[A-Za-z0-9-]*)/$',
        BlogDetailView.as_view(),
        name='blog_detail'
        ),
    ]
