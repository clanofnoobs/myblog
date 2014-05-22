# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Article.slug'
        db.delete_column(u'article_article', 'slug')

        # Adding field 'Article.slu'
        db.add_column(u'article_article', 'slu',
                      self.gf('django.db.models.fields.SlugField')(default='NULL', unique=True, max_length=50),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Article.slug'
        raise RuntimeError("Cannot reverse this migration. 'Article.slug' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Article.slug'
        db.add_column(u'article_article', 'slug',
                      self.gf('django.db.models.fields.SlugField')(max_length=50, unique=True),
                      keep_default=False)

        # Deleting field 'Article.slu'
        db.delete_column(u'article_article', 'slu')


    models = {
        u'article.article': {
            'Meta': {'object_name': 'Article'},
            'body': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'slu': ('django.db.models.fields.SlugField', [], {'default': "'NULL'", 'unique': 'True', 'max_length': '50'}),
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