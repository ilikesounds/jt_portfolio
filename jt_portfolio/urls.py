"""
jt_portfolio URL Configuration
This module is the root URL configuration for the jt_portfolio site.
"""
from django.conf.urls import url, include
from django.contrib import admin
from .views import Home

app_name = 'jt_portfolio'

urlpatterns = [
    url(r'^$', Home.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls')),
    url(r'^bcr/$', Home.as_view())
]

# url(r'^resume/', include('aboutme.urls')),
# url(r'^projects/', include('projects.urls'))
