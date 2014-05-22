# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Article.slugifiedtitle'
        db.add_column(u'article_article', 'slugifiedtitle',
                      self.gf('django.db.models.fields.SlugField')(max_length=50, unique=True, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Article.slugifiedtitle'
        db.delete_column(u'article_article', 'slugifiedtitle')


    models = {
        u'article.article': {
            'Meta': {'object_name': 'Article'},
            'body': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'slugifiedtitle': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'article.experiments': {
            'Meta': {'object_name': 'experiments'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'default': "'/no-image.jpg'", 'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['article']