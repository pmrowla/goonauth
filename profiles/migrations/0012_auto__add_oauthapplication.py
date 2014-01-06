# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'OAuthApplication'
        db.create_table(u'profiles_oauthapplication', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['oauth2_provider.Application'])),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'profiles', ['OAuthApplication'])


    def backwards(self, orm):
        # Deleting model 'OAuthApplication'
        db.delete_table(u'profiles_oauthapplication')


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
        u'oauth2_provider.application': {
            'Meta': {'object_name': 'Application'},
            'authorization_grant_type': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'client_id': ('django.db.models.fields.CharField', [], {'default': "u'k=YN_eI9uae.;!dF2yJQau=ItrEFxgedxm8Py5-2'", 'unique': 'True', 'max_length': '100'}),
            'client_secret': ('django.db.models.fields.CharField', [], {'default': "u'CLLYJQfFmPtCTaIlwbPpi4I!@AiwpphwdW6lxQ:;qeb.o!3HfvPjMGm@pG:hP;aahfZI:lK;IgmJ;WeqZv!oCQ9paPT0e9V83=Us5T-oW4YFtbjNBDU=_BL5UIf0MWu9'", 'max_length': '255', 'blank': 'True'}),
            'client_type': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'redirect_uris': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'profiles.battlefieldfourprofile': {
            'Meta': {'object_name': 'BattlefieldFourProfile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'profiles.blizzardprofile': {
            'Meta': {'object_name': 'BlizzardProfile'},
            'email': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'realid': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'profiles.eveonlineprofile': {
            'Meta': {'object_name': 'EveOnlineProfile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'profiles.leagueoflegendsprofile': {
            'Meta': {'object_name': 'LeagueOfLegendsProfile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'profiles.minecraftprofile': {
            'Meta': {'object_name': 'MinecraftProfile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'profiles.nintendoprofile': {
            'Meta': {'object_name': 'NintendoProfile'},
            'friendcode': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'profiles.oauthapplication': {
            'Meta': {'object_name': 'OAuthApplication'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['oauth2_provider.Application']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'profiles.playstationnetworkprofile': {
            'Meta': {'object_name': 'PlaystationNetworkProfile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'profiles.somethingawfulprofile': {
            'Meta': {'object_name': 'SomethingAwfulProfile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'postcount': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'regdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'userid': ('django.db.models.fields.TextField', [], {}),
            'username': ('django.db.models.fields.TextField', [], {})
        },
        u'profiles.steamprofile': {
            'Meta': {'object_name': 'SteamProfile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'userid': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'profiles.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'bf4': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profiles.BattlefieldFourProfile']", 'null': 'True', 'blank': 'True'}),
            'blizzard': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profiles.BlizzardProfile']", 'null': 'True', 'blank': 'True'}),
            'eveonline': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profiles.EveOnlineProfile']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'leagueoflegends': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profiles.LeagueOfLegendsProfile']", 'null': 'True', 'blank': 'True'}),
            'minecraft': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profiles.MinecraftProfile']", 'null': 'True', 'blank': 'True'}),
            'nintendo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profiles.NintendoProfile']", 'null': 'True', 'blank': 'True'}),
            'psn': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profiles.PlaystationNetworkProfile']", 'null': 'True', 'blank': 'True'}),
            'somethingawful': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['profiles.SomethingAwfulProfile']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'steam': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profiles.SteamProfile']", 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'verification_code': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'worldoftanks': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profiles.WorldOfTanksProfile']", 'null': 'True', 'blank': 'True'}),
            'xbl': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profiles.XboxLiveProfile']", 'null': 'True', 'blank': 'True'})
        },
        u'profiles.worldoftanksprofile': {
            'Meta': {'object_name': 'WorldOfTanksProfile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'profiles.xboxliveprofile': {
            'Meta': {'object_name': 'XboxLiveProfile'},
            'gamertag': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['profiles']