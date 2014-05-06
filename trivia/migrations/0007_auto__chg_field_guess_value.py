# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Guess.value'
        db.alter_column(u'trivia_guess', 'value', self.gf('django.db.models.fields.TextField')())

    def backwards(self, orm):

        # Changing field 'Guess.value'
        db.alter_column(u'trivia_guess', 'value', self.gf('django.db.models.fields.FloatField')())

    models = {
        u'trivia.guess': {
            'Meta': {'object_name': 'Guess'},
            'date_placed': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'placed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'trivia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['trivia.Trivia']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['trivia.Player']"}),
            'value': ('django.db.models.fields.TextField', [], {})
        },
        u'trivia.player': {
            'Meta': {'object_name': 'Player'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'trivia.trivia': {
            'Meta': {'object_name': 'Trivia'},
            'details': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'insider': ('django.db.models.fields.TextField', [], {}),
            'overview': ('django.db.models.fields.TextField', [], {}),
            'prize': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'trivia': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'unit': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['trivia']