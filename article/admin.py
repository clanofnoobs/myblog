from django.contrib import admin
from article.models import Article,experiments

class tinymce(admin.ModelAdmin):
   class Media:
           js = ('/static/js/tiny_mce/tiny_mce.js','/static/js/tiny_mce/textarea.js',)

admin.site.register(Article, tinymce)
admin.site.register(experiments)
