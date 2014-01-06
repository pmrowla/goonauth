from lxml import etree
import requests

from django.views.generic import TemplateView, FormView
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.contrib import messages
from django.views.generic.edit import UpdateView
from django.http import Http404

from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope
from oauth2_provider.models import Application

from rest_framework import generics, permissions, mixins

from braces.views import LoginRequiredMixin, FormValidMessageMixin

from profiles.somethingawful import SomethingAwful
from profiles.serializers import UserProfileSerializer
from profiles.models import  LeagueOfLegendsProfile, EveOnlineProfile, MinecraftProfile, \
    NintendoProfile, PlaystationNetworkProfile, XboxLiveProfile, BattlefieldFourProfile, \
    WorldOfTanksProfile, UserProfile, SomethingAwfulProfile, BlizzardProfile, OAuthApplication
from profiles.forms import SomethingAwfulForm, OAuthClientForm



somethingawful = SomethingAwful(settings.SA_USER, settings.SA_PASSWORD)


class OAuthClientCreateView(LoginRequiredMixin, FormView):
    template_name = "provider/new_client.html"
    form_class = OAuthClientForm
    success_url = "/"

    def form_valid(self, form):
        if Application.objects.filter(name=form.cleaned_data['application_name']).exists():
            messages.warning(self.request, "Application with this name already exists.")
        else:
            oapp = OAuthApplication()
            oapp.description = form.cleaned_data['description']
            oapp.website = form.cleaned_data['website']
        
            omodel = Application()
            omodel.user = self.request.user
            omodel.redirect_uris = form.cleaned_data['callback_url']
            omodel.client_type = 'confidential'
            omodel.authorization_grant_type = 'authorization-code'
            omodel.name = form.cleaned_data['application_name']
            omodel.save()

            oapp.client = omodel
            oapp.save()
            
            messages.success(self.request, "Application Created!")
        
        return super(OAuthClientCreateView, self).form_valid(form)


class OAuthClientUpdateView(LoginRequiredMixin, FormValidMessageMixin, UpdateView):
    template_name = "provider/edit_client.html"
    model = Application
    fields = ['redirect_uris', 'name']

    def get_object(self, *args, **kwargs):
        obj = super(OAuthClientUpdateView, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user:
            raise Http404
        
        return obj


class OAuthClientListView(TemplateView):
    template_name = "provider/list_clients.html"

    def get_context_data(self, *args, **kwargs):
        context = super(OAuthClientListView, self).get_context_data(*args, **kwargs)
        
        clients = Application.objects.filter(user=self.request.user)
        context['clients'] = clients

        return context


class HomepageView(TemplateView):
    template_name = "homepage.html"

    def get_context_data(self, *args, **kwargs):
        context = super(HomepageView, self).get_context_data(*args, **kwargs)

        if self.request.user.is_authenticated():
            profile = UserProfile.objects.get(user=self.request.user)
        else:
            profile = None

        context.update({
            'profile': profile,
        })

        return context

    
class SteamProfileSettingsView(TemplateView):
    template_name = "games/steam.html"

    def post(self, *args, **kwargs):
        profile = UserProfile.objects.get(user=self.request.user)
        
        if self.request.POST.get('steamurl'):
            steam_data = self.get_steam_data(self.request.POST['steamurl'] + '?xml=1')
            if steam_data:
                steam = profile.steam
                steam.username = steam_data['username']
                steam.url = self.request.POST['steamurl']
                steam.userid = steam_data['id']
                steam.save()
                messages.info(self.request, "Updated your steam profile")
            else:
                messages.warning(self.request, "Unable to parse steam profile URL. Please make sure it is set to public and exists.")
        else:
            messages.warning(self.request, "No URL submitted. Please try again.")

        return self.render_to_response(self.get_context_data())

    def get_context_data(self, *args, **kwargs):
        context = super(SteamProfileSettingsView, self).get_context_data(*args, **kwargs)
        profile = UserProfile.objects.get(user=self.request.user)
        steam = profile.steam

        context['steam'] = steam

        return context
        

    def get_steam_data(self, url):
        steam_profile = {}

        try:
            tree = etree.fromstring(requests.get(url).content)
        except:
            return None
        
        id64 = tree.xpath('/profile/steamID64/text()')[0]
        username = tree.xpath('/profile/steamID/text()')[0]

        steam_profile['id'] = id64
        steam_profile['username'] = username
        return steam_profile
        


class LeagueOfLegendsProfileSettingsView(LoginRequiredMixin, FormValidMessageMixin, UpdateView):
    template_name = "games/league.html"
    success_url = '/profile/league/'
    model = LeagueOfLegendsProfile
    form_valid_message = "Update Successful"

    def get_object(self, queryset=None):
        profile = UserProfile.objects.get(user=self.request.user)
        league = profile.leagueoflegends
        return league


class EveOnlineProfileSettingsView(LoginRequiredMixin, FormValidMessageMixin, UpdateView):
    template_name = "games/eve.html"
    success_url = '/profile/eve/'
    model = EveOnlineProfile
    form_valid_message = "Update Successful"

    def get_object(self, queryset=None):
        profile = UserProfile.objects.get(user=self.request.user)
        eve = profile.eveonline
        return eve


class MinecraftProfileSettingsView(LoginRequiredMixin, FormValidMessageMixin, UpdateView):
    template_name = "games/minecraft.html"
    success_url = '/profile/minecraft/'
    model = MinecraftProfile
    form_valid_message = "Update Successful"

    def get_object(self, queryset=None):
        profile = UserProfile.objects.get(user=self.request.user)
        minecraft = profile.minecraft
        return minecraft


class NintendoProfileSettingsView(LoginRequiredMixin, FormValidMessageMixin, UpdateView):
    template_name = "games/nintendo.html"
    success_url = '/profile/nintendo/'
    model = NintendoProfile
    form_valid_message = "Update Successful"

    def get_object(self, queryset=None):
        profile = UserProfile.objects.get(user=self.request.user)
        nintendo = profile.nintendo
        return nintendo


class PlaystationNetworkProfileSettingsView(LoginRequiredMixin, FormValidMessageMixin, UpdateView):
    template_name = "games/psn.html"
    success_url = '/profile/psn/'
    model = PlaystationNetworkProfile
    form_valid_message = "Update Successful"

    def get_object(self, queryset=None):
        profile = UserProfile.objects.get(user=self.request.user)
        psn = profile.psn
        return psn
    

class XboxLiveProfileSettingsView(LoginRequiredMixin, FormValidMessageMixin, UpdateView):
    template_name = "games/xbl.html"
    success_url = '/profile/xbox/'
    model = XboxLiveProfile
    form_valid_message = "Update Successful"
    
    def get_object(self, queryset=None):
        profile = UserProfile.objects.get(user=self.request.user)
        xbl = profile.xbl
        return xbl


class BattlefieldFourProfileSettingsView(LoginRequiredMixin, FormValidMessageMixin, UpdateView):
    template_name = "games/bf4.html"
    success_url = '/profile/bf4/'
    model = BattlefieldFourProfile
    form_valid_message = "Update Successful"

    def get_object(self, queryset=None):
        profile = UserProfile.objects.get(user=self.request.user)
        bf4 = profile.bf4
        return bf4


class WorldOfTanksProfileSettingsView(LoginRequiredMixin, FormValidMessageMixin, UpdateView):
    template_name = "games/wot.html"
    success_url = '/profile/wot/'
    model = WorldOfTanksProfile
    form_valid_message = "Update Successful"

    def get_object(self, queryset=None):
        profile = UserProfile.objects.get(user=self.request.user)
        wot = profile.worldoftanks
        return wot


class BlizzardProfileSettingsView(LoginRequiredMixin, FormValidMessageMixin, UpdateView):
    template_name = "games/blizzard.html"
    success_url = '/profile/blizzard/'
    model = BlizzardProfile
    form_valid_message = "Update Successful"

    def get_object(self, queryset=None):
        profile = UserProfile.objects.get(user=self.request.user)
        blizz = profile.blizzard
        return blizz

    
class AccountSettingsView(TemplateView):
    template_name = "account/settings.html"

    def post(self, *args, **kwargs):
        profile = UserProfile.objects.get(user=self.request.user)
        if 'isvisible' in self.request.POST:
            profile.visible = True
        else:
            profile.visible = False

        profile.save()

        return self.render_to_response(self.get_context_data())


    def get_context_data(self, *args, **kwargs):
        context = super(AccountSettingsView, self).get_context_data(*args, **kwargs)
        user = self.request.user
        profile = UserProfile.objects.get(user=user)
        context['profile'] = profile

        return context


class SAVerificationView(FormView):
    template_name = "account/somethingawful.html"
    form_class = SomethingAwfulForm
    success_url = '/profile/somethingawful/'

    def form_valid(self, form):
        url = form.cleaned_data['url']
        user = self.request.user
        profile = UserProfile.objects.get(user=user)

        try:
            sa_profile = somethingawful.get_profile(url)
            print sa_profile
        except:
            messages.warning(self.request, "There was an error parsing your SA profile. Please try again or contact elgruntox.")
            return super(SAVerificationView, self).form_valid(form)

        if profile.active:
            sa = profile.somethingawful
            sa.username = sa_profile['username']
            sa.postcount = sa_profile['postcount']
            sa.regdate = sa_profile['regdate']
            sa.save()

            messages.success(self.request, "SA Profile Successfully Synced")
            return super(SAVerificationView, self).form_valid(form)
            
        succeeded = False

        for k, v in sa_profile.items():
            if succeeded:
                pass
            else:
                if v == profile.verification_code:
                    sa = SomethingAwfulProfile()
                    sa.username = sa_profile['username']
                    sa.url = url
                    sa.userid = sa_profile['userid']
                    sa.postcount = sa_profile['postcount']
                    sa.regdate = sa_profile['regdate']
                    sa.save()
                
                    profile.somethingawful = sa
                    profile.active = True
                    profile.save()

                    messages.success(self.request, "Welcome to the site! You are now a verified Goon. Thanks for signing up.")
                    succeeded = True
                
        
        if not succeeded:
            messages.warning(self.request, "Unable to find your verfication code in the supplied profile. Please try again.")

        return super(SAVerificationView, self).form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(SAVerificationView, self).get_context_data(*args, **kwargs)

        user = self.request.user
        profile = UserProfile.objects.get(user=user)
        context['profile'] = profile

        return context


class ProfileDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    model = UserProfile
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.filter(active=True).filter(visible=True)


class ProfileList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    model = UserProfile
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.filter(active=True).filter(visible=True)


class ProfileUserDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    model = UserProfile
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.filter(active=True)

    def get(self, request, *args, **kwargs):
        user = request.user
        profile = get_object_or_404(UserProfile, user=user)

        self.kwargs['pk'] = profile.id
        kwargs['pk'] = profile.id
        
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        user = request.user
        profile = get_object_or_404(UserProfile, user=user)

        self.kwargs['pk'] = profile.id
        kwargs['pk'] = profile.id

        return self.update(request, *args, **kwargs)
