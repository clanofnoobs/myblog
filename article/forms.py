from django import forms
from models import Article
from tinymce.widgets import TinyMCE

class ArticleForm(forms.ModelForm):
   class Meta:
        model = Article
        fields = ('title', 'body', 'pub_date')
        

     
