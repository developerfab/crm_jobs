# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Empresa'
        db.create_table(u'core_empresa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('nit', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=13)),
            ('direccion', self.gf('django.db.models.fields.TextField')()),
            ('descripcion', self.gf('django.db.models.fields.TextField')()),
            ('sitio_web', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'core', ['Empresa'])


        # Renaming column for 'Oferta.empresa' to match new field type.
        db.rename_column(u'core_oferta', 'empresa', 'empresa_id')
        # Changing field 'Oferta.empresa'
        db.alter_column(u'core_oferta', 'empresa_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Empresa']))
        # Adding index on 'Oferta', fields ['empresa']
        db.create_index(u'core_oferta', ['empresa_id'])


    def backwards(self, orm):
        # Removing index on 'Oferta', fields ['empresa']
        db.delete_index(u'core_oferta', ['empresa_id'])

        # Deleting model 'Empresa'
        db.delete_table(u'core_empresa')


        # Renaming column for 'Oferta.empresa' to match new field type.
        db.rename_column(u'core_oferta', 'empresa_id', 'empresa')
        # Changing field 'Oferta.empresa'
        db.alter_column(u'core_oferta', 'empresa', self.gf('django.db.models.fields.CharField')(max_length=100))

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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.desarrollador': {
            'Meta': {'object_name': 'Desarrollador'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'perfil_bitbucked': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'perfil_github': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'perfil_linkedin': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'perfil_twitter': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'tecnologias': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Tecnologia']", 'through': u"orm['core.TecnologiaDesarrollador']", 'symmetrical': 'False'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '13'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'core.empresa': {
            'Meta': {'object_name': 'Empresa'},
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'direccion': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nit': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'sitio_web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '13'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'core.oferta': {
            'Meta': {'object_name': 'Oferta'},
            'aplicantes': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Desarrollador']", 'symmetrical': 'False'}),
            'beneficios': ('django.db.models.fields.TextField', [], {}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Empresa']"}),
            'estado': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'funciones': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'salario': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            'tecnologias': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['core.Tecnologia']", 'through': u"orm['core.TecnologiaOferta']", 'symmetrical': 'False'})
        },
        u'core.tecnologia': {
            'Meta': {'object_name': 'Tecnologia'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'core.tecnologiadesarrollador': {
            'Meta': {'object_name': 'TecnologiaDesarrollador'},
            'desarrollador': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Desarrollador']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nivel': ('django.db.models.fields.IntegerField', [], {}),
            'tecnologia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Tecnologia']"})
        },
        u'core.tecnologiaoferta': {
            'Meta': {'object_name': 'TecnologiaOferta'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nivel': ('django.db.models.fields.IntegerField', [], {}),
            'oferta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Oferta']"}),
            'tecnologia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Tecnologia']"})
        }
    }

    complete_apps = ['core']