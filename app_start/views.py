from django.shortcuts import render
from .models import PersonOfLivingSociety, News


def index(request):
    return render(request, "index.html")


def news(request):
    news = News.objects.all()
    if request.user.id:
        client = PersonOfLivingSociety.objects.get(id_account=request.user.id)
        return render(request, "metrostroi/news.html", {"client": client, "news": news})
    else:
        return render(request, "metrostroi/news.html", {"news": news})


def servers(request):
    if request.user.id:
        client = PersonOfLivingSociety.objects.get(id_account=request.user.id)
        return render(request, "metrostroi/servers.html", {"client": client})
    else:
        return render(request, "metrostroi/servers.html")


def requests(request):
    if request.user.id:
        client = PersonOfLivingSociety.objects.get(id_account=request.user.id)
        return render(request, "metrostroi/requests.html", {"client": client})
    else:
        return render(request, "metrostroi/requests.html")


def complaints(request):
    if request.user.id:
        client = PersonOfLivingSociety.objects.get(id_account=request.user.id)
        return render(request, "metrostroi/complaint.html", {"client": client})
    else:
        return render(request, "metrostroi/complaint.html")

