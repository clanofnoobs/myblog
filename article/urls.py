from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^all/$', 'article.views.articles'),
    url(r'^get/(?P<post_id>\d+)/$', 'article.views.post'),
	url(r'^create/$', 'article.views.create'),
        url(r'^webgl/$', 'article.views.webgl'),

)
