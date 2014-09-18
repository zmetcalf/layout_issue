# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HiddenpageLayout'
        db.create_table(u'widgets_hiddenpagelayout', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'widgets', ['HiddenpageLayout'])


    def backwards(self, orm):
        # Deleting model 'HiddenpageLayout'
        db.delete_table(u'widgets_hiddenpagelayout')


    models = {
        u'widgets.hiddenpagelayout': {
            'Meta': {'object_name': 'HiddenpageLayout'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'widgets.homepagelayout': {
            'Meta': {'object_name': 'HomepageLayout'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'widgets.whateverpagelayout': {
            'Meta': {'object_name': 'WhateverpageLayout'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['widgets']