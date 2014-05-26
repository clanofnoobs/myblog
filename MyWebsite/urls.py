from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from MyWebsite.views import ExperimentsView
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^posts/', include('article.urls')),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^$', 'article.views.articles'),	
    url(r'^logout$', 'MyWebsite.views.logout'),
    url(r'^invalidlogin$', 'MyWebsite.views.invalidlogin'),
    url(r'^loggedin$', 'article.views.loggedin'),
    url(r'^auth$', 'article.views.auth'),
    url(r'^photos$', 'article.views.photos'),
    url(r'^about$', 'article.views.about'),
    url(r'^experiments', 'article.views.experiments'),
    url(r'^projects', 'article.views.projects'),
    #url(r'^webgl/$', TemplateView.as_view(template_name="webgl.html")),
    url(r'^webgl/$', ExperimentsView.as_view(link="webgl.html")),
    url(r'^cuberotation/$', ExperimentsView.as_view(link="cuberotation.html")),
    url(r'^lighting/$', ExperimentsView.as_view(link="lighting.html")),
    url(r'^sphere/$', ExperimentsView.as_view(link="sphere.html")),
    url(r'^trackball/$', ExperimentsView.as_view(link="trackball.html")),
    url(r'^blogposts/$', 'article.views.post_list'),
    url(r'^blogposts/(?P<pk>[0-9]+)/$', 'article.views.post_detail'),


    # Examples:
    # url(r'^$', 'MyWebsite.views.home', name='home'),
    # url(r'^MyWebsite/', include('MyWebsite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
