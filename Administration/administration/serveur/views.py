from django.shortcuts import render, get_object_or_404, redirect
from . import models
from .forms import typeServeurForm, SeveursForm, ServicesForm, ApplicationsForm, UtilisateursForm, RessourcesForm


def index(request):
    Serveurs = models.Serveurs.objects.all()
    return render(request, "serveur/index.html", {"Serveurs" : Serveurs})

# --- TYPE SERVEUR ---
def list_type_serveur(request):
    types = models.TypeServeurs.objects.all()
    return render(request, "serveur/type_serveurs.html", {"types": types})

def add_type_serveur(request):
    if request.method == "POST":
        form = typeServeurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_type_serveur")
    else:
        form = typeServeurForm()
    return render(request, "serveur/type_serveurs_form.html", {"form": form})

def update_type_serveur(request, id):
    type_srv = get_object_or_404(models.TypeServeurs, pk=id)
    if request.method == "POST":
        form = typeServeurForm(request.POST, instance=type_srv)
        if form.is_valid():
            form.save()
            return redirect("list_type_serveur")
    else:
        form = typeServeurForm(instance=type_srv)
    return render(request, "serveur/type_serveurs_form.html", {"form": form, "id": id})

def delete_type_serveur(request, id):
    type_srv = get_object_or_404(models.TypeServeurs, pk=id)
    type_srv.delete()
    return redirect("list_type_serveur")

# --- SERVEUR ---
def list_serveurs(request):
    serveurs = models.Serveurs.objects.all()
    return render(request, "serveur/serveurs.html", {"serveurs": serveurs})

def add_serveur(request):
    if request.method == "POST":
        form = SeveursForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_serveurs")
    else:
        form = SeveursForm()
    return render(request, "serveur/serveurs_form.html", {"form": form})

def update_serveur(request, id):
    serveur = get_object_or_404(models.Serveurs, pk=id)
    if request.method == "POST":
        form = SeveursForm(request.POST, instance=serveur)
        if form.is_valid():
            form.save()
            return redirect("list_serveurs")
    else:
        form = SeveursForm(instance=serveur)
    return render(request, "serveur/serveurs_form.html", {"form": form, "id": id})

def delete_serveur(request, id):
    serveur = get_object_or_404(models.Serveurs, pk=id)
    serveur.delete()
    return redirect("list_serveurs")

# --- SERVICE ---
def list_services(request):
    services = models.Services.objects.all()
    return render(request, "serveur/service.html", {"services": services})

def add_service(request):
    if request.method == "POST":
        form = ServicesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_services")
    else:
        form = ServicesForm()
    return render(request, "serveur/service_form.html", {"form": form})

def update_service(request, id):
    service = get_object_or_404(models.Services, pk=id)
    if request.method == "POST":
        form = ServicesForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect("list_services")
    else:
        form = ServicesForm(instance=service)
    return render(request, "serveur/service_form.html", {"form": form, "id": id})

def delete_service(request, id):
    service = get_object_or_404(models.Services, pk=id)
    service.delete()
    return redirect("list_services")

# --- UTILISATEUR ---
def list_utilisateurs(request):
    utilisateurs = models.Utilisateurs.objects.all()
    return render(request, "serveur/users.html", {"utilisateurs": utilisateurs})

def add_utilisateur(request):
    if request.method == "POST":
        form = UtilisateursForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_utilisateurs")
    else:
        form = UtilisateursForm()
    return render(request, "serveur/utilisateur_form.html", {"form": form})

def update_utilisateur(request, id):
    utilisateur = get_object_or_404(models.Utilisateurs, pk=id)
    if request.method == "POST":
        form = UtilisateursForm(request.POST, instance=utilisateur)
        if form.is_valid():
            form.save()
            return redirect("list_utilisateurs")
    else:
        form = UtilisateursForm(instance=utilisateur)
    return render(request, "serveur/utilisateur_form.html", {"form": form, "id": id})

def delete_utilisateur(request, id):
    utilisateur = get_object_or_404(models.Utilisateurs, pk=id)
    utilisateur.delete()
    return redirect("list_utilisateurs")

# --- APPLICATION ---
def list_applications(request):
    applications = models.Applications.objects.all()
    return render(request, "serveur/application.html", {"applications": applications})

def add_application(request):
    if request.method == "POST":
        form = ApplicationsForm(request.POST, request.FILES)  # <-- IMPORTANT
        if form.is_valid():
            form.save()
            return redirect("list_applications")
    else:
        form = ApplicationsForm()
    return render(request, "serveur/application_form.html", {"form": form})

def update_application(request, id):
    application = get_object_or_404(models.Applications, pk=id)
    if request.method == "POST":
        form = ApplicationsForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            return redirect("list_applications")
    else:
        form = ApplicationsForm(instance=application)
    return render(request, "serveur/application_form.html", {"form": form, "id": id})

def delete_application(request, id):
    application = get_object_or_404(models.Applications, pk=id)
    application.delete()
    return redirect("list_applications")

# --- USAGE RESSOURCE ---
def list_usageressources(request):
    usages = models.Ressources.objects.all()
    return render(request, "serveur/usageressource_list.html", {"usages": usages})

def add_usageressource(request):
    if request.method == "POST":
        form = RessourcesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_usageressources")
    else:
        form = RessourcesForm()
    return render(request, "serveur/usageressource_form.html", {"form": form})

def update_usageressource(request, id):
    usage = get_object_or_404(models.Ressources, pk=id)
    if request.method == "POST":
        form = RessourcesForm(request.POST, instance=usage)
        if form.is_valid():
            form.save()
            return redirect("list_usageressources")
    else:
        form = RessourcesForm(instance=usage)
    return render(request, "serveur/usageressource_form.html", {"form": form, "id": id})

def delete_usageressource(request, id):
    usage = get_object_or_404(models.Ressources, pk=id)
    usage.delete()
    return redirect("list_usageressources")
