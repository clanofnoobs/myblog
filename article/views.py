from django.shortcuts import render_to_response, redirect
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from article.models import Article
from forms import ArticleForm
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf

def projects(request):
   return render_to_response('projects.html', context_instance=RequestContext(request))

def experiments(request):
   return render_to_response('experiments.html', context_instance=RequestContext(request))

def about(request):
   return render_to_response('about.html', context_instance=RequestContext(request))

@login_required(login_url='/invalidlogin')
def loggedin(request):
   return render_to_response('loggedin.html', context_instance=RequestContext(request))

def auth(request):
   username = request.POST.get('username', '')
   password = request.POST.get('password', '')
   user = authenticate(username=username, password=password)
   
   if user is not None:
      login(request, user)
      return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
   else:
     
      return HttpResponseRedirect('/invalidlogin')

def articles(request):
   posts = Article.objects.all().order_by("-pub_date")
   paginator = Paginator(posts, 3)
   d = dict(posts=posts, user= request.user)
   d.update(csrf(request))
   try: page = int(request.GET.get("page", '1'))
   except ValueError: page = 1

   try:
       posts = paginator.page(page)
   except (InvalidPage, EmptyPage):
       posts = paginator.page(paginator.num_pages)
       
   
   return render_to_response('articles.html', d, context_instance=RequestContext(request))

def webgl(request):
   return render_to_response("webgl.html", context_instance=RequestContext(request))
   

def post(request, post_id=1):
   return render_to_response('article.html', {'post':Article.objects.get(id=post_id) }, context_instance=RequestContext(request))
   
@login_required(login_url='/invalidlogin')
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
         
            return HttpResponseRedirect('/articles/all')
    else:
        form = ArticleForm()
        
    args = {}
    args.update(csrf(request))
    
    args['form'] = form
    
    return render_to_response('create_article.html', args, context_instance=RequestContext(request))
  
