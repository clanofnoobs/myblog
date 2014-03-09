from django.db import models
from tinymce import models as tinymce_models

class Article(models.Model):
   title = models.CharField(max_length=30)
   body = models.TextField()
   pub_date = models.DateTimeField('date published')
   likes = models.IntegerField(default=0)
   
   
def __unicode__(self):
   return self.title
   
	

# Create your models here.
