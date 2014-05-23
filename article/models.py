from django.db import models
from django.db.models.fields.files import ImageField
from tinymce import models as tinymce_models
from django.template.defaultfilters import slugify



class Article(models.Model):
   title = models.CharField(max_length=30)
   body = models.TextField()
   slugifiedtitle = models.SlugField(unique=True,null=True)
   pub_date = models.DateTimeField('date published')
    

   def __unicode__(self):
       return self.title
   
class Photo(models.Model):
   image = models.ImageField(upload_to = "media/")
   description = models.CharField(max_length=40)

class experiments(models.Model):
   title = models.CharField(max_length=20)
   thumbnail = models.ImageField(upload_to="/")

   def __unicode__(self):
      return self.title


