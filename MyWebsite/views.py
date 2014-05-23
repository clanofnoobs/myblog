from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from django.views.generic.base import View

def invalidlogin(request):
   c={}
   c.update(csrf(request))
   if request.user.is_authenticated():
       return HttpResponseRedirect('/')
   return render_to_response('invalidlogin.html', c)

def logout(request):
   auth.logout(request)
   return redirect(request.META.get('HTTP_REFERER','/'))

class ExperimentsView(View):
  link = ""
  
  def get(self,request):
     return render_to_response(self.link, context_instance=RequestContext(request))


