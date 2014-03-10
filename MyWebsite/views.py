from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib import auth

def invalidlogin(request):
   return render_to_response('invalidlogin.html')

def logout(request):
   auth.logout(request)
   return redirect('article.views.articles')

def photos(request):
   return render_to_response('photos.html', context_instance=RequestContext(request))
