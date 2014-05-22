from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^all/$', 'article.views.articles'),
    url(r'^(?P<postslug>.*)/$', 'article.views.post'),
	url(r'^create/$', 'article.views.create'),

)
