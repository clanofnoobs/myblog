from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^articles/', include('article.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^$', 'article.views.articles'),	
    url(r'^logout$', 'MyWebsite.views.logout'),
    url(r'^invalidlogin$', 'MyWebsite.views.invalidlogin'),
    url(r'^loggedin$', 'article.views.loggedin'),
    url(r'^auth$', 'article.views.auth'),
    url(r'^photos$', 'MyWebsite.views.photos'),
    url(r'^about$', 'article.views.about'),
    url(r'^experiments', 'article.views.experiments'),
    url(r'^projects', 'article.views.projects'),
    # Examples:
    # url(r'^$', 'MyWebsite.views.home', name='home'),
    # url(r'^MyWebsite/', include('MyWebsite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
