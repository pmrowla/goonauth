from rest_framework import serializers
from profiles.models import *



class SteamProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SteamProfile
        fields = ('username', 'url', 'userid',)


class SomethingAwfulProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SomethingAwfulProfile
        fields = ('username', 'url', 'userid', 'postcount', 'regdate',)


class LeagueOfLegendsProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeagueOfLegendsProfile
        fields = ('username',)


class EveOnlineProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = EveOnlineProfile
        fields = ('username',)


class MinecraftProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MinecraftProfile
        fields = ('username',)


class NintendoProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = NintendoProfile
        fields = ('friendcode',)


class PlaystationNetworkProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaystationNetworkProfile
        fields = ('username',)


class XboxLiveProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = XboxLiveProfile
        fields = ('gamertag',)


class BattlefieldFourProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BattlefieldFourProfile
        fields = ('username',)


class BlizzardProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlizzardProfile
        fields = ('realid', 'email',)
        

class WorldOfTanksProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorldOfTanksProfile
        fields = ('username',)
        

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)

        
class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    somethingawful = SomethingAwfulProfileSerializer()
    steam = SteamProfileSerializer()
    leagueoflegends = LeagueOfLegendsProfileSerializer()
    eveonline = EveOnlineProfileSerializer()
    minecraft = MinecraftProfileSerializer()
    nintendo = NintendoProfileSerializer()
    psn = PlaystationNetworkProfileSerializer()
    xbl = XboxLiveProfileSerializer()
    bf4 = BattlefieldFourProfileSerializer()
    blizzard = BlizzardProfileSerializer()
    worldoftanks = WorldOfTanksProfileSerializer()
    
    class Meta:
        model = UserProfile
        fields = (
            'user',
            'active',
            'visible',
            'somethingawful',
            'steam',
            'eveonline',
            'minecraft',
            'nintendo',
            'psn',
            'xbl',
            'bf4',
            'blizzard',
            'worldoftanks'
        )
