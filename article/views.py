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
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET','POST'])
def post_list(request,format=None):
   if request.method == 'GET':
      posts = Article.objects.all()
      serializer = ArticleSerializer(posts,many=True)
      return Response(serializer.data)
   elif request.method == 'POST':
      serializer = ArticleSerializer(data=request.DATA)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def post_detail(request,pk,format=None):
   try:
      post = Article.objects.get(pk=pk)
   except Post.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
   if request.method == 'GET':
      serializer = ArticleSerializer(post)
      return Response(serializer.data)
   elif request.method == 'PUT':
      serializer = ArticleSerializer(post,data=request.DATA)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   elif request.method == 'DELETE':
      post.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)

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
  
