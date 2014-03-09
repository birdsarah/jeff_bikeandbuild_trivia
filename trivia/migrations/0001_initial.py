# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'trivia_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal(u'trivia', ['User'])

        # Adding model 'Trivia'
        db.create_table(u'trivia_trivia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('trivia', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('overview', self.gf('django.db.models.fields.TextField')()),
            ('insider', self.gf('django.db.models.fields.TextField')()),
            ('details', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'trivia', ['Trivia'])

        # Adding model 'Guess'
        db.create_table(u'trivia_guess', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value', self.gf('django.db.models.fields.FloatField')()),
            ('trivia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['trivia.Trivia'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['trivia.User'])),
            ('placed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date_placed', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'trivia', ['Guess'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'trivia_user')

        # Deleting model 'Trivia'
        db.delete_table(u'trivia_trivia')

        # Deleting model 'Guess'
        db.delete_table(u'trivia_guess')


    models = {
        u'trivia.guess': {
            'Meta': {'object_name': 'Guess'},
            'date_placed': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'placed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'trivia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['trivia.Trivia']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['trivia.User']"}),
            'value': ('django.db.models.fields.FloatField', [], {})
        },
        u'trivia.trivia': {
            'Meta': {'object_name': 'Trivia'},
            'details': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'insider': ('django.db.models.fields.TextField', [], {}),
            'overview': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'trivia': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        u'trivia.user': {
            'Meta': {'object_name': 'User'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['trivia']