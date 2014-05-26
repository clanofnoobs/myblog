from django.shortcuts import render_to_response, redirect
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from article.models import Article, Photo
from forms import ArticleForm
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from article.serializers import ArticleSerializer,PhotoSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

class JSONResponse(HttpResponse):
   def __init__(self,data,**kwargs):
      content = JSONRenderer().render(data)
      kwargs['content_type'] = 'application/json'
      super(JSONResponse,self).__init__(content, **kwargs)


@csrf_exempt
def post_list(request):
   if request.method == 'GET':
      posts = Article.objects.all()
      serializer = ArticleSerializer(posts,many=True)
      return JSONResponse(serializer.data)
   elif request.method == 'POST':
      data = JSONParser().parse(request)
      serializer = ArticleSerializer(data=data)
      if serializer.is_valid():
         serializer.save()
         return JSONResponse(serializer.data, status=201)
      return JSONResponse(serializer.errors,status=400)

@csrf_exempt
def post_detail(request,pk):
   try:
      post = Article.objects.get(pk=pk)
   except:
      return HttpResponse(status=404)
   if request.method == 'GET':
      serializer = ArticleSerializer(post)
      return JSONResponse(serializer.data)
   elif request.method == 'PUT':
      data = JSONParser().parse(post, data=data)
      if serializer.is_valid():
         serializer.save()
         return JSONResponse(serializer.data)
      return JSONResponse(serializer.errors, status=400)
   elif request.method == 'DELETE':
      post.delete()
      return HttpResponse(status=204)

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

def photos(request):
   photos = Photo.objects.all()
   context = {'photos': photos}

   return render_to_response('photos.html',context,context_instance=RequestContext(request))
   
  

def post(request, postslug):
   post = Article.objects.get(slugifiedtitle=postslug)
   context = {'post':post}
   return render_to_response('article.html', context, context_instance=RequestContext(request))
   
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
  
