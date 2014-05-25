from article.models import Article, Photo
from rest_framework import serializers 

class ArticleSerializer(serializers.ModelSerializer):
   class Meta:
      model = Article
      fields = {'pub_date','body','title'}


class PhotoSerializer(serializers.ModelSerializer):
   class Meta:
      model = Photo
      fields = {'image','description'}
