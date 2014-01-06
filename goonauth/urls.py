from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

from profiles.views import ProfileDetail, ProfileUserDetail, ProfileList, HomepageView, \
    SAVerificationView, AccountSettingsView, EveOnlineProfileSettingsView, SteamProfileSettingsView, \
    LeagueOfLegendsProfileSettingsView, NintendoProfileSettingsView, MinecraftProfileSettingsView, \
    PlaystationNetworkProfileSettingsView, XboxLiveProfileSettingsView, BattlefieldFourProfileSettingsView, \
    WorldOfTanksProfileSettingsView, BlizzardProfileSettingsView, OAuthClientCreateView, OAuthClientListView, \
    OAuthClientUpdateView


urlpatterns = patterns("",
    url(r"^$", HomepageView.as_view(), name="home"),
    url(r"^admin/", include(admin.site.urls)),

    url(r"^account/", include("account.urls")),

    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
                       
    url(r'^oauth/new/', OAuthClientCreateView.as_view(), name="newoauth"),
    url(r'^oauth/clients/', OAuthClientListView.as_view(), name="listoauth"),

    url(r'^api/profiles/', ProfileList.as_view()),
    url(r'^api/profiles/user/', ProfileUserDetail.as_view()),
    url(r'^api/profiles/(?P<pk>[0-9]+)/$', ProfileDetail.as_view()),

    url(r'^profile/somethingawful/', SAVerificationView.as_view(), name="somethingawful"), 
    url(r"^profile/settings/", AccountSettingsView.as_view(), name="accountsettings"),
    url(r"^profile/steam/", SteamProfileSettingsView.as_view(), name="steamsettings"),
    url(r"^profile/eve/", EveOnlineProfileSettingsView.as_view(), name="eveonlinesettings"),
    url(r"^profile/league/", LeagueOfLegendsProfileSettingsView.as_view(), name="leaguesettings"),
    url(r"^profile/minecraft/", MinecraftProfileSettingsView.as_view(), name="minecraftsettings"),
    url(r"^profile/nintendo/", NintendoProfileSettingsView.as_view(), name="nintendosettings"),
    url(r"^profile/psn/", PlaystationNetworkProfileSettingsView.as_view(), name="psnsettings"),
    url(r"^profile/xbox/", XboxLiveProfileSettingsView.as_view(), name="xblsettings"),
    url(r"^profile/bf4/", BattlefieldFourProfileSettingsView.as_view(), name="bf4settings"),
    url(r"^profile/wot/", WorldOfTanksProfileSettingsView.as_view(), name="wotsettings"),
    url(r"^profile/blizzard/", BlizzardProfileSettingsView.as_view(), name="blizzardsettings"),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
