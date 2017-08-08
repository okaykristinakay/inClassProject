"""postproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from records import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
#the first view is regex. then it will create a view. the dollar sign means that it is empty. if there is nothing there then it will return all the information on the homepage
    url(r'^$', views.PostListView.as_view(), name='list_posts'),
    url(r'^(?P<pk>\d+)/$', views.PostDetailView.as_view(), name='detail_post'),
]
