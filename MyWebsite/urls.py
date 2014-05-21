from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from MyWebsite import ExperimentsView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^posts/', include('article.urls')),
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
    #url(r'^webgl/$', 'article.views.webgl'),
    url(r'^cuberotation/$', 'article.views.cuberotation'),
    url(r'^lighting/$', 'article.views.lighting'),
    url(r'^sphere/$', 'article.views.sphere'),
    url(r'^trackball/$','article.views.trackball'),
    #url(r'^webgl/$', TemplateView.as_view(template_name="webgl.html")),
    url(r'^webgl/$', ExperimentsView.as_view(link="webgl.html")),

    # Examples:
    # url(r'^$', 'MyWebsite.views.home', name='home'),
    # url(r'^MyWebsite/', include('MyWebsite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
