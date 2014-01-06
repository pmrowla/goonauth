from django import forms

from profiles.models import SteamProfile, LeagueOfLegendsProfile, \
    EveOnlineProfile, MinecraftProfile, NintendoProfile, PlaystationNetworkProfile, \
    XboxLiveProfile, BattlefieldFourProfile, WorldOfTanksProfile



class OAuthClientForm(forms.Form):
    callback_url = forms.URLField(help_text="Where should we return after successfully authenticating?")
    website = forms.URLField(help_text="Your application's publicly accessible home page, where users can go to download, make use of, or find out more information about your application.")
    application_name = forms.CharField(help_text="Your application name.")
    description = forms.CharField(help_text="Your application description, which will be shown in user-facing authorization screens. ")
    

class SomethingAwfulForm(forms.Form):
    url = forms.URLField(help_text="URL to Your SomethingAwful Profile")


class SteamProfileForm(forms.ModelForm):
    class Meta:
        model = SteamProfile


class LeagueOfLegendsProfileForm(forms.Form):
    class Meta:
        model = LeagueOfLegendsProfile


class EveOnlineProfileForm(forms.ModelForm):
    class Meta:
        model = EveOnlineProfile


class MinecraftProfileForm(forms.ModelForm):
    class Meta:
        model = MinecraftProfile


class NintendoProfileForm(forms.ModelForm):
    class Meta:
        model = NintendoProfile


class PlaystationNetworkProfileForm(forms.ModelForm):
    class Meta:
        model = PlaystationNetworkProfile


class XboxLiveProfileForm(forms.ModelForm):
    class Meta:
        model = XboxLiveProfile


class BattlefieldFourProfileForm(forms.ModelForm):
    class Meta:
        model = BattlefieldFourProfile


class WorldOfTanksProfileForm(forms.ModelForm):
    class Meta:
        model = WorldOfTanksProfile
