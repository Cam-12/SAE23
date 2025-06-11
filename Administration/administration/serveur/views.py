from django.shortcuts import render, HttpResponseRedirect
from . import models

def index(request):
    Serveurs = models.Serveurs.objects.all()
    return render(request, "serveur/index.html", {"Serveurs" : Serveurs})

def users(request):
    Utilisateurs = models.Utilisateurs.objects.all()
    return render (request, "serveur/users.html", {"Utilisateurs" : Utilisateurs})