from django.db import models
from django.db.models.fields.files import ImageField
from tinymce import models as tinymce_models


class Article(models.Model):
   title = models.CharField(max_length=30)
   body = models.TextField()
   pub_date = models.DateTimeField('date published')
    
   def __unicode__(self):
       return self.title
   
#class album(models.Model):
  # image = models.ImageField(upload_to = '/', default = '/no-img.jpg')
  # description = models.CharField(max_length=40)

class experiments(models.Model):
   title = models.CharField(max_length=20)
   thumbnail = models.ImageField(upload_to="/",default = '/no-image.jpg')

   def __unicode__(self):
      return self.title


