from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf

def invalidlogin(request):
   c={}
   c.update(csrf(request))
   if request.user.is_authenticated():
       return HttpResponseRedirect('/')
   return render_to_response('invalidlogin.html', c)

def logout(request):
   auth.logout(request)
   return redirect('article.views.articles')

def photos(request):
   return render_to_response('photos.html', context_instance=RequestContext(request))
