from django.contrib import admin

from profiles.models import SteamProfile, SomethingAwfulProfile, LeagueOfLegendsProfile, \
    EveOnlineProfile, MinecraftProfile, NintendoProfile, PlaystationNetworkProfile, \
    XboxLiveProfile, BattlefieldFourProfile, WorldOfTanksProfile, UserProfile



admin.site.register(SteamProfile)
admin.site.register(SomethingAwfulProfile)
admin.site.register(LeagueOfLegendsProfile)
admin.site.register(EveOnlineProfile)
admin.site.register(MinecraftProfile)
admin.site.register(NintendoProfile)
admin.site.register(PlaystationNetworkProfile)
admin.site.register(XboxLiveProfile)
admin.site.register(BattlefieldFourProfile)
admin.site.register(WorldOfTanksProfile)
admin.site.register(UserProfile)

