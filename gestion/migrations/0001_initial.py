# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Universidad'
        db.create_table(u'gestion_universidad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('nombre_universidad', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'gestion', ['Universidad'])

        # Adding model 'Revista'
        db.create_table(u'gestion_revista', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('nombre_revista', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'gestion', ['Revista'])

        # Adding model 'Docente'
        db.create_table(u'gestion_docente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('credito', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'gestion', ['Docente'])

        # Adding model 'Area'
        db.create_table(u'gestion_area', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre_area', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'gestion', ['Area'])

        # Adding model 'TipoPublicacion'
        db.create_table(u'gestion_tipopublicacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre_tipo', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal(u'gestion', ['TipoPublicacion'])

        # Adding model 'Docente_Area'
        db.create_table(u'gestion_docente_area', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('docente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gestion.Docente'], null=None, blank=None)),
            ('area', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gestion.Area'], null=None, blank=None)),
        ))
        db.send_create_signal(u'gestion', ['Docente_Area'])

        # Adding model 'Publicacion'
        db.create_table(u'gestion_publicacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('universidad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gestion.Universidad'], null=True, blank=True)),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('fecha_inicio', self.gf('django.db.models.fields.DateField')()),
            ('fecha_fin', self.gf('django.db.models.fields.DateField')()),
            ('lugar', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=350)),
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gestion.TipoPublicacion'])),
        ))
        db.send_create_signal(u'gestion', ['Publicacion'])

        # Adding model 'AreasPublicacion'
        db.create_table(u'gestion_areaspublicacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('area', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gestion.Area'], null=None, blank=None)),
            ('publicacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gestion.Publicacion'], null=None, blank=None)),
        ))
        db.send_create_signal(u'gestion', ['AreasPublicacion'])


    def backwards(self, orm):
        # Deleting model 'Universidad'
        db.delete_table(u'gestion_universidad')

        # Deleting model 'Revista'
        db.delete_table(u'gestion_revista')

        # Deleting model 'Docente'
        db.delete_table(u'gestion_docente')

        # Deleting model 'Area'
        db.delete_table(u'gestion_area')

        # Deleting model 'TipoPublicacion'
        db.delete_table(u'gestion_tipopublicacion')

        # Deleting model 'Docente_Area'
        db.delete_table(u'gestion_docente_area')

        # Deleting model 'Publicacion'
        db.delete_table(u'gestion_publicacion')

        # Deleting model 'AreasPublicacion'
        db.delete_table(u'gestion_areaspublicacion')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'gestion.area': {
            'Meta': {'object_name': 'Area'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_area': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'gestion.areaspublicacion': {
            'Meta': {'object_name': 'AreasPublicacion'},
            'area': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gestion.Area']", 'null': 'None', 'blank': 'None'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publicacion': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gestion.Publicacion']", 'null': 'None', 'blank': 'None'})
        },
        u'gestion.docente': {
            'Meta': {'object_name': 'Docente'},
            'credito': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'gestion.docente_area': {
            'Meta': {'object_name': 'Docente_Area'},
            'area': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gestion.Area']", 'null': 'None', 'blank': 'None'}),
            'docente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gestion.Docente']", 'null': 'None', 'blank': 'None'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'gestion.publicacion': {
            'Meta': {'object_name': 'Publicacion'},
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'fecha_fin': ('django.db.models.fields.DateField', [], {}),
            'fecha_inicio': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '350'}),
            'lugar': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gestion.TipoPublicacion']"}),
            'universidad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gestion.Universidad']", 'null': 'True', 'blank': 'True'})
        },
        u'gestion.revista': {
            'Meta': {'object_name': 'Revista'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_revista': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'gestion.tipopublicacion': {
            'Meta': {'object_name': 'TipoPublicacion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_tipo': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        u'gestion.universidad': {
            'Meta': {'object_name': 'Universidad'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_universidad': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['gestion']