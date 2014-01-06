from rest_framework import serializers
from profiles.models import *



class SteamProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SteamProfile


class SomethingAwfulProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SomethingAwfulProfile


class LeagueOfLegendsProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeagueOfLegendsProfile


class EveOnlineProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = EveOnlineProfile


class MinecraftProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MinecraftProfile


class NintendoProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = NintendoProfile


class PlaystationNetworkProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaystationNetworkProfile


class XboxLiveProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = XboxLiveProfile


class BattlefieldFourProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BattlefieldFourProfile


class BlizzardProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlizzardProfile
        

class WorldOfTanksProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorldOfTanksProfile
        

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
