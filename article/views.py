from django.shortcuts import render_to_response
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from article.models import Article
from forms import ArticleForm
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf



def articles(request):
   articles = Article.objects.all().order_by("-pub_date")
   paginator = Paginator(articles, 2)

   try: page = int(request.GET.get("page", '1'))
   except ValueError: page = 1

   try:
       articles = paginator.page(page)
   except (InvalidPage, EmptyPage):
       articles = paginator.page(paginator.num_pages)

   return render_to_response('articles.html', dict(articles=articles, user=request.user))
   

def article(request, article_id=1):
   return render_to_response('article.html', {'article':Article.objects.get(id=article_id) })
   

def create(request):
    if request.POST:
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        
            
            return HttpResponseRedirect('/articles/all')
    else:
        form = ArticleForm()
        
    args = {}
    args.update(csrf(request))
    
    args['form'] = form
    
    return render_to_response('create_article.html', args)
  

