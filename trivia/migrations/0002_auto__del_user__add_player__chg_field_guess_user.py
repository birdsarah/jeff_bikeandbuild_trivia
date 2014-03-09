# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'trivia_user')

        # Adding model 'Player'
        db.create_table(u'trivia_player', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal(u'trivia', ['Player'])


        # Changing field 'Guess.user'
        db.alter_column(u'trivia_guess', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['trivia.Player']))

    def backwards(self, orm):
        # Adding model 'User'
        db.create_table(u'trivia_user', (
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'trivia', ['User'])

        # Deleting model 'Player'
        db.delete_table(u'trivia_player')


        # Changing field 'Guess.user'
        db.alter_column(u'trivia_guess', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['trivia.User']))

    models = {
        u'trivia.guess': {
            'Meta': {'object_name': 'Guess'},
            'date_placed': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'placed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'trivia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['trivia.Trivia']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['trivia.Player']"}),
            'value': ('django.db.models.fields.FloatField', [], {})
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
            'insider': ('django.db.models.fields.TextField', [], {}),
            'overview': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'trivia': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['trivia']