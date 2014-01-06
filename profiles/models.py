import string
import random

from django.db import models
from django.contrib.auth.models import User

from oauth2_provider.models import Application


required = { 'null': True, 'blank': True }


class OAuthApplication(models.Model):
    client = models.ForeignKey(Application)
    description = models.TextField()
    website = models.URLField()

    def __unicode__(self):
        return self.client.name


class SteamProfile(models.Model):
    username = models.CharField(max_length=50, **required)
    url = models.URLField(**required)
    userid = models.CharField(max_length=25, **required)

    def __unicode__(self):
        return self.username


class SomethingAwfulProfile(models.Model):
    username = models.TextField()
    url = models.URLField()
    userid = models.TextField()
    postcount = models.IntegerField(**required)
    regdate = models.DateField(**required)

    def __unicode__(self):
        return self.username


class LeagueOfLegendsProfile(models.Model):
    username = models.CharField(max_length=50, **required)

    def __unicode__(self):
        return self.username


class EveOnlineProfile(models.Model):
    username = models.CharField(max_length=50, **required)

    def __unicode__(self):
        return self.username


class MinecraftProfile(models.Model):
    username = models.CharField(max_length=50, **required)

    def __unicode__(self):
        return self.username


class NintendoProfile(models.Model):
    friendcode = models.CharField(max_length=50, **required)

    def __unicode__(self):
        return self.friendcode


class PlaystationNetworkProfile(models.Model):
    username = models.CharField(max_length=50, **required)

    def __unicode__(self):
        return self.username


class XboxLiveProfile(models.Model):
    gamertag = models.CharField(max_length=50, **required)

    def __unicode__(self):
        return self.gamertag


class BattlefieldFourProfile(models.Model):
    username = models.CharField(max_length=50, **required)

    def __unicode__(self):
        return self.username


class BlizzardProfile(models.Model):
    realid = models.CharField(max_length=50, **required)
    email = models.CharField(max_length=50, **required)

    def __unicode__(self):
        return self.realid


class WorldOfTanksProfile(models.Model):
    username = models.CharField(max_length=50, **required)

    def __unicode__(self):
        return self.username


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    verification_code = models.TextField(**required)
    active = models.BooleanField(default=False)
    visible = models.BooleanField(default=True)

    somethingawful = models.OneToOneField(SomethingAwfulProfile, **required)
    steam = models.ForeignKey(SteamProfile, **required)
    leagueoflegends = models.ForeignKey(LeagueOfLegendsProfile, **required)
    eveonline = models.ForeignKey(EveOnlineProfile, **required)
    minecraft = models.ForeignKey(MinecraftProfile, **required)
    nintendo = models.ForeignKey(NintendoProfile, **required)
    psn = models.ForeignKey(PlaystationNetworkProfile, **required)
    xbl = models.ForeignKey(XboxLiveProfile, **required)
    bf4 = models.ForeignKey(BattlefieldFourProfile, **required)
    blizzard = models.ForeignKey(BlizzardProfile, **required)
    worldoftanks = models.ForeignKey(WorldOfTanksProfile, **required)

    def generate_random_code(self, size=20, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))

    def save(self, *args, **kwargs):
        if self.verification_code is None:
            self.verification_code = self.generate_random_code()

        super(UserProfile, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.user.username
    
    
