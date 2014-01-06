from django.dispatch import receiver

from account.signals import password_changed
from account.signals import user_sign_up_attempt, user_signed_up
from account.signals import user_login_attempt, user_logged_in

from eventlog.models import log

from profiles.models import SteamProfile, LeagueOfLegendsProfile, \
    EveOnlineProfile, MinecraftProfile, NintendoProfile, PlaystationNetworkProfile, \
    XboxLiveProfile, BattlefieldFourProfile, WorldOfTanksProfile, UserProfile, BlizzardProfile


@receiver(user_logged_in)
def handle_user_logged_in(sender, **kwargs):
    log(
        user=kwargs.get("user"),
        action="USER_LOGGED_IN",
        extra={}
    )


@receiver(password_changed)
def handle_password_changed(sender, **kwargs):
    log(
        user=kwargs.get("user"),
        action="PASSWORD_CHANGED",
        extra={}
    )


@receiver(user_login_attempt)
def handle_user_login_attempt(sender, **kwargs):
    log(
        user=None,
        action="LOGIN_ATTEMPTED",
        extra={
            "username": kwargs.get("username"),
            "result": kwargs.get("result")
        }
    )


@receiver(user_sign_up_attempt)
def handle_user_sign_up_attempt(sender, **kwargs):
    log(
        user=None,
        action="SIGNUP_ATTEMPTED",
        extra={
            "username": kwargs.get("username"),
            "email": kwargs.get("email"),
            "result": kwargs.get("result")
        }
    )


@receiver(user_signed_up)
def handle_user_signed_up(sender, **kwargs):
    log(
        user=kwargs.get("user"),
        action="USER_SIGNED_UP",
        extra={}
    )

    profile = UserProfile()
    profile.user = kwargs.get("user")
    profile.save()

    steam = SteamProfile()
    steam.username = "None"
    steam.url = "None"
    steam.save()

    lol = LeagueOfLegendsProfile()
    lol.username = "None"
    lol.save()
    
    eve = EveOnlineProfile()
    eve.username = "None"
    eve.save()
    
    minecraft = MinecraftProfile()
    minecraft.username = "None"
    minecraft.save()
    
    nintendo = NintendoProfile()
    nintendo.username = "None"
    nintendo.friendcode = "None"
    nintendo.save()
    
    psn = PlaystationNetworkProfile()
    psn.username = "None"
    psn.save()
    
    xbl = XboxLiveProfile()
    xbl.gamertag = "None"
    xbl.save()
    
    bf4 = BattlefieldFourProfile()
    bf4.username = "None"
    bf4.save()
    
    blizz = BlizzardProfile()
    blizz.realid = "None"
    blizz.email = "None"
    blizz.save()
    
    wot = WorldOfTanksProfile()
    wot.username = "None"
    wot.save()

    profile.steam = steam
    profile.leagueoflegends = lol
    profile.eveonline = eve
    profile.minecraft = minecraft
    profile.nintendo = nintendo
    profile.psn = psn
    profile.xbl = xbl
    profile.bf4 = bf4
    profile.blizzard = blizz
    profile.worldoftanks = wot

    profile.save()
