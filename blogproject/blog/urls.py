from django.conf.urls import url
from . import views
app_name = 'blog'
urlpatterns = [
    url(r'^$', views.portfolio, name='portfolio'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
    url(r'^index2$', views.index2, name='index2'),
    url(r'^portfolio$', views.portfolio, name='portfolio'),
    url(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag'),
    #url(r'^portfolio_page$', views.portfolio_page, name='portfolio_page'),
]