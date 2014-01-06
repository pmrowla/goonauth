# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SteamProfile'
        db.create_table(u'profiles_steamprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.TextField')()),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('steam_id', self.gf('django.db.models.fields.TextField')()),
            ('steam_id_64', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'profiles', ['SteamProfile'])

        # Adding model 'SomethingAwfulProfile'
        db.create_table(u'profiles_somethingawfulprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('verified', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('username', self.gf('django.db.models.fields.TextField')()),
            ('user_id', self.gf('django.db.models.fields.IntegerField')()),
            ('avatar', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'profiles', ['SomethingAwfulProfile'])

        # Adding model 'LeagueOfLegendsProfile'
        db.create_table(u'profiles_leagueoflegendsprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'profiles', ['LeagueOfLegendsProfile'])

        # Adding model 'EveOnlineProfile'
        db.create_table(u'profiles_eveonlineprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'profiles', ['EveOnlineProfile'])

        # Adding model 'MinecraftProfile'
        db.create_table(u'profiles_minecraftprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'profiles', ['MinecraftProfile'])

        # Adding model 'NintendoProfile'
        db.create_table(u'profiles_nintendoprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.TextField')()),
            ('friendcode', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'profiles', ['NintendoProfile'])

        # Adding model 'PlaystationNetworkProfile'
        db.create_table(u'profiles_playstationnetworkprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'profiles', ['PlaystationNetworkProfile'])

        # Adding model 'XboxLiveProfile'
        db.create_table(u'profiles_xboxliveprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('gamertag', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'profiles', ['XboxLiveProfile'])

        # Adding model 'BattlefieldFourProfile'
        db.create_table(u'profiles_battlefieldfourprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'profiles', ['BattlefieldFourProfile'])

        # Adding model 'BlizzardProfile'
        db.create_table(u'profiles_blizzardprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('realid', self.gf('django.db.models.fields.TextField')()),
            ('email', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'profiles', ['BlizzardProfile'])

        # Adding model 'WorldOfTanksProfile'
        db.create_table(u'profiles_worldoftanksprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'profiles', ['WorldOfTanksProfile'])

        # Adding model 'UserProfile'
        db.create_table(u'profiles_userprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('somethingawful', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['profiles.SomethingAwfulProfile'], unique=True, null=True, blank=True)),
            ('steam', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profiles.SteamProfile'], null=True, blank=True)),
            ('leageoflegends', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profiles.LeagueOfLegendsProfile'], null=True, blank=True)),
            ('eveonline', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profiles.EveOnlineProfile'], null=True, blank=True)),
            ('minecraft', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profiles.MinecraftProfile'], null=True, blank=True)),
            ('nintendo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profiles.NintendoProfile'], null=True, blank=True)),
            ('psn', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profiles.PlaystationNetworkProfile'], null=True, blank=True)),
            ('xbl', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profiles.XboxLiveProfile'], null=True, blank=True)),
            ('bf4', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profiles.BattlefieldFourProfile'], null=True, blank=True)),
            ('blizzard', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profiles.BlizzardProfile'], null=True, blank=True)),
            ('worldoftanks', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profiles.WorldOfTanksProfile'], null=True, blank=True)),
        ))
        db.send_create_signal(u'profiles', ['UserProfile'])


    def backwards(self, orm):
        # Deleting model 'SteamProfile'
        db.delete_table(u'profiles_steamprofile')

        # Deleting model 'SomethingAwfulProfile'
        db.delete_table(u'profiles_somethingawfulprofile')

        # Deleting model 'LeagueOfLegendsProfile'
        db.delete_table(u'profiles_leagueoflegendsprofile')

        # Deleting model 'EveOnlineProfile'
        db.delete_table(u'profiles_eveonlineprofile')

        # Deleting model 'MinecraftProfile'
        db.delete_table(u'profiles_minecraftprofile')

        # Deleting model 'NintendoProfile'
        db.delete_table(u'profiles_nintendoprofile')

        # Deleting model 'PlaystationNetworkProfile'
        db.delete_table(u'profiles_playstationnetworkprofile')

        # Deleting model 'XboxLiveProfile'
        db.delete_table(u'profiles_xboxliveprofile')

        # Deleting model 'BattlefieldFourProfile'
        db.delete_table(u'profiles_battlefieldfourprofile')

        # Deleting model 'BlizzardProfile'
        db.delete_table(u'profiles_blizzardprofile')

        # Deleting model 'WorldOfTanksProfile'
        db.delete_table(u'profiles_worldoftanksprofile')

        # Deleting model 'UserProfile'
        db.delete_table(u'profiles_userprofile')


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
            'username': ('django.db.models.fields.TextField', [], {})
        },
        u'profiles.blizzardprofile': {
            'Meta': {'object_name': 'BlizzardProfile'},
            'email': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'realid': ('django.db.models.fields.TextField', [], {})
        },
        u'profiles.eveonlineprofile': {
            'Meta': {'object_name': 'EveOnlineProfile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'username': ('django.db.models.fields.TextField', [], {})
        },
        u'profiles.leagueoflegendsprofile': {
            'Meta': {'object_name': 'LeagueOfLegendsProfile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'username': ('django.db.models.fields.TextField', [], {})
        },
        u'profiles.minecraftprofile': {
            'Meta': {'object_name': 'MinecraftProfile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'username': ('django.db.models.fields.TextField', [], {})
        },
        u'profiles.nintendoprofile': {
            'Meta': {'object_name': 'NintendoProfile'},
            'friendcode': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'username': ('django.db.models.fields.TextField', [], {})
        },
        u'profiles.playstationnetworkprofile': {
            'Meta': {'object_name': 'PlaystationNetworkProfile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'username': ('django.db.models.fields.TextField', [], {})
        },
        u'profiles.somethingawfulprofile': {
            'Meta': {'object_name': 'SomethingAwfulProfile'},
            'avatar': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user_id': ('django.db.models.fields.IntegerField', [], {}),
            'username': ('django.db.models.fields.TextField', [], {}),
            'verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'profiles.steamprofile': {
            'Meta': {'object_name': 'SteamProfile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'steam_id': ('django.db.models.fields.TextField', [], {}),
            'steam_id_64': ('django.db.models.fields.TextField', [], {}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'username': ('django.db.models.fields.TextField', [], {})
        },
        u'profiles.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'bf4': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profiles.BattlefieldFourProfile']", 'null': 'True', 'blank': 'True'}),
            'blizzard': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profiles.BlizzardProfile']", 'null': 'True', 'blank': 'True'}),
            'eveonline': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profiles.EveOnlineProfile']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'leageoflegends': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profiles.LeagueOfLegendsProfile']", 'null': 'True', 'blank': 'True'}),
            'minecraft': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profiles.MinecraftProfile']", 'null': 'True', 'blank': 'True'}),
            'nintendo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profiles.NintendoProfile']", 'null': 'True', 'blank': 'True'}),
            'psn': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profiles.PlaystationNetworkProfile']", 'null': 'True', 'blank': 'True'}),
            'somethingawful': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['profiles.SomethingAwfulProfile']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'steam': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profiles.SteamProfile']", 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'worldoftanks': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profiles.WorldOfTanksProfile']", 'null': 'True', 'blank': 'True'}),
            'xbl': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profiles.XboxLiveProfile']", 'null': 'True', 'blank': 'True'})
        },
        u'profiles.worldoftanksprofile': {
            'Meta': {'object_name': 'WorldOfTanksProfile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'username': ('django.db.models.fields.TextField', [], {})
        },
        u'profiles.xboxliveprofile': {
            'Meta': {'object_name': 'XboxLiveProfile'},
            'gamertag': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['profiles']