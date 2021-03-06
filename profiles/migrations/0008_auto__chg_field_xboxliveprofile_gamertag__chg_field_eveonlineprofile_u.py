# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'XboxLiveProfile.gamertag'
        db.alter_column(u'profiles_xboxliveprofile', 'gamertag', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'EveOnlineProfile.username'
        db.alter_column(u'profiles_eveonlineprofile', 'username', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'PlaystationNetworkProfile.username'
        db.alter_column(u'profiles_playstationnetworkprofile', 'username', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'LeagueOfLegendsProfile.username'
        db.alter_column(u'profiles_leagueoflegendsprofile', 'username', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))
        # Deleting field 'SteamProfile.steam_id'
        db.delete_column(u'profiles_steamprofile', 'steam_id')

        # Deleting field 'SteamProfile.steam_id_64'
        db.delete_column(u'profiles_steamprofile', 'steam_id_64')


        # Changing field 'SteamProfile.username'
        db.alter_column(u'profiles_steamprofile', 'username', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'SteamProfile.url'
        db.alter_column(u'profiles_steamprofile', 'url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

        # Changing field 'BattlefieldFourProfile.username'
        db.alter_column(u'profiles_battlefieldfourprofile', 'username', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'NintendoProfile.username'
        db.alter_column(u'profiles_nintendoprofile', 'username', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'NintendoProfile.friendcode'
        db.alter_column(u'profiles_nintendoprofile', 'friendcode', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'BlizzardProfile.email'
        db.alter_column(u'profiles_blizzardprofile', 'email', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'BlizzardProfile.realid'
        db.alter_column(u'profiles_blizzardprofile', 'realid', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'WorldOfTanksProfile.username'
        db.alter_column(u'profiles_worldoftanksprofile', 'username', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'MinecraftProfile.username'
        db.alter_column(u'profiles_minecraftprofile', 'username', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

    def backwards(self, orm):

        # Changing field 'XboxLiveProfile.gamertag'
        db.alter_column(u'profiles_xboxliveprofile', 'gamertag', self.gf('django.db.models.fields.TextField')(default='Gaymer'))

        # Changing field 'EveOnlineProfile.username'
        db.alter_column(u'profiles_eveonlineprofile', 'username', self.gf('django.db.models.fields.TextField')(default='Gayemr'))

        # Changing field 'PlaystationNetworkProfile.username'
        db.alter_column(u'profiles_playstationnetworkprofile', 'username', self.gf('django.db.models.fields.TextField')(default='Gaymer'))

        # Changing field 'LeagueOfLegendsProfile.username'
        db.alter_column(u'profiles_leagueoflegendsprofile', 'username', self.gf('django.db.models.fields.TextField')(default='Gaymer'))
        # Adding field 'SteamProfile.steam_id'
        db.add_column(u'profiles_steamprofile', 'steam_id',
                      self.gf('django.db.models.fields.TextField')(default='Gaymer'),
                      keep_default=False)

        # Adding field 'SteamProfile.steam_id_64'
        db.add_column(u'profiles_steamprofile', 'steam_id_64',
                      self.gf('django.db.models.fields.TextField')(default='Gaymer'),
                      keep_default=False)


        # Changing field 'SteamProfile.username'
        db.alter_column(u'profiles_steamprofile', 'username', self.gf('django.db.models.fields.TextField')(default='Gaymer'))

        # Changing field 'SteamProfile.url'
        db.alter_column(u'profiles_steamprofile', 'url', self.gf('django.db.models.fields.URLField')(default='Gaymer', max_length=200))

        # Changing field 'BattlefieldFourProfile.username'
        db.alter_column(u'profiles_battlefieldfourprofile', 'username', self.gf('django.db.models.fields.TextField')(default='Gaymer'))

        # Changing field 'NintendoProfile.username'
        db.alter_column(u'profiles_nintendoprofile', 'username', self.gf('django.db.models.fields.TextField')(default='Gaymer'))

        # Changing field 'NintendoProfile.friendcode'
        db.alter_column(u'profiles_nintendoprofile', 'friendcode', self.gf('django.db.models.fields.TextField')(default='Gaymer'))

        # Changing field 'BlizzardProfile.email'
        db.alter_column(u'profiles_blizzardprofile', 'email', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'BlizzardProfile.realid'
        db.alter_column(u'profiles_blizzardprofile', 'realid', self.gf('django.db.models.fields.TextField')(default='Gaymer'))

        # Changing field 'WorldOfTanksProfile.username'
        db.alter_column(u'profiles_worldoftanksprofile', 'username', self.gf('django.db.models.fields.TextField')(default='Gaymer'))

        # Changing field 'MinecraftProfile.username'
        db.alter_column(u'profiles_minecraftprofile', 'username', self.gf('django.db.models.fields.TextField')(default='Gaymer'))

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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'profiles.playstationnetworkprofile': {
            'Meta': {'object_name': 'PlaystationNetworkProfile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'profiles.somethingawfulprofile': {
            'Meta': {'object_name': 'SomethingAwfulProfile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'userid': ('django.db.models.fields.TextField', [], {}),
            'username': ('django.db.models.fields.TextField', [], {})
        },
        u'profiles.steamprofile': {
            'Meta': {'object_name': 'SteamProfile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
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
            'verification_code': ('django.db.models.fields.TextField', [], {}),
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