"""
jt_portfolio URL Configuration
This module is the root URL configuration for the jt_portfolio site.
"""
from django.conf.urls import url, include
from django.contrib import admin
from .views import redirect_home


urlpatterns = [
    url(r'^$', redirect_home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls')),
]

# url(r'^resume/', include('aboutme.urls')),
# url(r'^projects/', include('projects.urls'))
