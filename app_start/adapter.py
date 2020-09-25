from app_start.models import PersonOfLivingSociety
from project_sun.settings import STEAM_APIKEY

from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
import requests as rq


class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        url = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={apikey}&steamids={steamid}"
        if not sociallogin.account.uid:
            return

        info = sociallogin.account.uid.split("/")
        data = rq.get(url.format(apikey=STEAM_APIKEY, steamid=info[-1]))
        data = data.json()

        try:
            person = PersonOfLivingSociety.objects.get(steamid=data['response']['players'][0]['steamid'])
            person.nick = data['response']['players'][0]['personaname']
            person.avatar = data['response']['players'][0]['avatarfull']
            person.steamid = data['response']['players'][0]['steamid']
            person.url = data['response']['players'][0]['profileurl']
            person.save()
        except PersonOfLivingSociety.DoesNotExist:
            PersonOfLivingSociety.objects.get_or_create(
                id_account=len(PersonOfLivingSociety.objects.all()) + 2,
                nick=data['response']['players'][0]['personaname'],
                avatar=data['response']['players'][0]['avatarfull'],
                steamid=data['response']['players'][0]['steamid'],
                url=data['response']['players'][0]['profileurl'])
        except Exception:
            pass
