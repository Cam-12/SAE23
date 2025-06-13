from django.shortcuts import render, get_object_or_404, redirect
from . import models
from .models import Serveurs, Services, Utilisateurs, TypeServeurs, Applications, Ressources
from .forms import typeServeurForm, SeveursForm, ServicesForm, ApplicationsForm, UtilisateursForm, RessourcesForm, ImportForm
from django.contrib import messages
import csv
from django.core.files import File
from django.http import HttpResponse


def index(request):
    serveurs = Serveurs.objects.all()
    nb_services = Services.objects.count()
    nb_serveurs = serveurs.count()
    nb_utilisateurs = Utilisateurs.objects.count()

    serveurs_stats = []

    for s in serveurs:
        services_sur_serveur = Services.objects.filter(serveur_lanc=s)

        total_ram_used = sum(svc.ram_ness for svc in services_sur_serveur)
        total_cpu_used = sum(svc.cpu for svc in services_sur_serveur)
        total_disk_used = sum(svc.disk for svc in services_sur_serveur)

        serveurs_stats.append({
            "nom": s.nom,
            "ram_utilisee": total_ram_used,
            "ram_dispo": s.ram - total_ram_used,
            "cpu_utilise": total_cpu_used,
            "cpu_dispo": s.cpu - total_cpu_used,
            "disk_utilise": total_disk_used,
            "disk_dispo": s.disk - total_disk_used,
        })

    return render(request, 'serveur/index.html', {
        'nb_services': nb_services,
        'nb_serveurs': nb_serveurs,
        'nb_utilisateurs': nb_utilisateurs,
        'serveurs_stats': serveurs_stats
    })

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

def import_serveur(request):
    if request.method == 'POST':
        form = ImportForm(request.POST, request.FILES)
        if form.is_valid():
            fichier = request.FILES['fichier']
            # Ici, on suppose que le fichier est un CSV
            try:
                data = fichier.read().decode('utf-8').splitlines()
                reader = csv.DictReader(data)
                for row in reader:
                    Serveurs.objects.create(
                        nom=row['nom'],
                        type=TypeServeurs.objects.get(id=row['type_id']),  # ou autre logique pour le type
                        cpu=int(row['cpu']),
                        ram=int(row['ram']),
                        disk=int(row['disk'])
                    )
                messages.success(request, "Importation réussie !")
            except Exception as e:
                messages.error(request, f"Erreur lors de l'import : {str(e)}")
            return redirect('list_serveurs')
    else:
        form = ImportForm()
    return render(request, 'serveur/import_serveur.html', {'form': form})

def import_type_serveur(request):
    if request.method == 'POST':
        form = ImportForm(request.POST, request.FILES)
        if form.is_valid():
            fichier = request.FILES['fichier']
            # Ici, on suppose que le fichier est un CSV
            try:
                data = fichier.read().decode('utf-8').splitlines()
                reader = csv.DictReader(data)
                for row in reader:
                    TypeServeurs.objects.create(
                        type=row['type'],
                        description=row['description']
                    )
                messages.success(request, "Importation réussie !")
            except Exception as e:
                messages.error(request, f"Erreur lors de l'import : {str(e)}")
            return redirect('list_type_serveur')
    else:
        form = ImportForm()
    return render(request, 'serveur/import_type_serveur.html', {'form': form})

def import_service(request):
    if request.method == 'POST':
        form = ImportForm(request.POST, request.FILES)
        if form.is_valid():
            fichier = request.FILES['fichier']
            # Ici, on suppose que le fichier est un CSV
            try:
                data = fichier.read().decode('utf-8').splitlines()
                reader = csv.DictReader(data)
                for row in reader:
                    Services.objects.create(
                        nom=row['nom'],
                        date_lancement=row['date_lancement'],
                        ram_util=int(row['ram_util']),
                        ram_ness=int(row['ram_util']),
                        serveur_lanc=Serveurs.objects.get(id=row['serveur_lanc_id']),
                        cpu=int(row['cpu']),
                        disk=int(row['disk'])
                    )
                messages.success(request, "Importation réussie !")
            except Exception as e:
                messages.error(request, f"Erreur lors de l'import : {str(e)}")
            return redirect('list_services')
    else:
        form = ImportForm()
    return render(request, 'serveur/import_service.html', {'form': form})

def import_utilisateur(request):
    if request.method == 'POST':
        form = ImportForm(request.POST, request.FILES)
        if form.is_valid():
            fichier = request.FILES['fichier']
            # Ici, on suppose que le fichier est un CSV
            try:
                data = fichier.read().decode('utf-8').splitlines()
                reader = csv.DictReader(data)
                for row in reader:
                    Utilisateurs.objects.create(
                        nom=row['nom'],
                        prenom=row['prenom'],
                        email=row['email']
                    )
                messages.success(request, "Importation réussie !")
            except Exception as e:
                messages.error(request, f"Erreur lors de l'import : {str(e)}")
            return redirect('list_utilisateurs')
    else:
        form = ImportForm()
    return render(request, 'serveur/import_utilisateur.html', {'form': form})


def import_application(request):
    if request.method == 'POST':
        form = ImportForm(request.POST, request.FILES)
        if form.is_valid():
            fichier = request.FILES['fichier']
            try:
                data = fichier.read().decode('utf-8').splitlines()
                reader = csv.DictReader(data)

                for row in reader:
                    # Création de l'application sans le ManyToMany
                    application = Applications.objects.create(
                        nom=row['nom'],
                        logo=row['logo'],  # Le nom du fichier doit être dans le CSV
                        utilisateur=Utilisateurs.objects.get(id=row['utilisateur_id']),
                        cpu=int(row['cpu']),
                        ram=int(row['ram']),
                        disk=int(row['disk'])
                    )

                    # Gestion du ManyToMany pour les services
                    services_ids = [int(id) for id in row['services'].split(',')]
                    for service_id in services_ids:
                        service = Services.objects.get(id=service_id)
                        # Création de la relation via la table intermédiaire Ressources
                        Ressources.objects.create(
                            application=application,
                            service=service
                        )

                    # Gestion de l'upload du logo
                    if row['logo']:
                        application.logo.save(
                            row['logo'],
                            File(open(f'chemin/vers/logos/{row['logo']}', 'rb')),
                            save=True
                        )

                messages.success(request, "Importation réussie !")
            except Exception as e:
                messages.error(request, f"Erreur lors de l'import : {str(e)}")
            return redirect('list_applications')
    else:
        form = ImportForm()
    return render(request, 'serveur/import_application.html', {'form': form})

def export_serveurs_csv(request):
    # Récupère tous les serveurs
    serveurs = Serveurs.objects.all()
    # Crée la réponse HTTP avec le type CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="serveurs.csv"'
    writer = csv.writer(response)
    # Écrit l’en-tête
    writer.writerow(['nom', 'type_id', 'cpu', 'ram', 'disk'])
    # Écrit les données
    for serveur in serveurs:
        writer.writerow([
            serveur.nom,
            serveur.type,
            serveur.cpu,
            serveur.ram,
            serveur.disk
        ])
    return response

def export_type_serveurs_csv(request):
    # Récupère tous les serveurs
    type_serveurs = TypeServeurs.objects.all()
    # Crée la réponse HTTP avec le type CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="type_serveurs.csv"'
    writer = csv.writer(response)
    # Écrit l’en-tête
    writer.writerow(['type', 'description'])
    # Écrit les données
    for type_serveur in type_serveurs:
        writer.writerow([
            type_serveur.type,
            type_serveur.description
        ])
    return response

def export_services_csv(request):
    # Récupère tous les serveurs
    services = Services.objects.all()
    # Crée la réponse HTTP avec le type CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="services.csv"'
    writer = csv.writer(response)
    # Écrit l’en-tête
    writer.writerow(['nom', 'date_lancement', 'ram_util', 'ram_ness', 'serveur_lanc_id', 'cpu', 'disk'])
    # Écrit les données
    for service in services:
        writer.writerow([
            service.nom,
            service.date_lancement,
            service.ram_util,
            service.ram_ness,
            service.serveur_lanc_id,
            service.cpu,
            service.disk
        ])
    return response

def export_utilisateurs_csv(request):
    # Récupère tous les serveurs
    utilisateurs = Utilisateurs.objects.all()
    # Crée la réponse HTTP avec le type CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="utilisateurs.csv"'
    writer = csv.writer(response)
    # Écrit l’en-tête
    writer.writerow(['nom', 'prenom', 'email'])
    # Écrit les données
    for utilisateur in utilisateurs:
        writer.writerow([
            utilisateur.nom,
            utilisateur.prenom,
            utilisateur.email
        ])
    return response

def export_applications_csv(request):
    # Récupère tous les serveurs
    applications = Applications.objects.all()
    # Crée la réponse HTTP avec le type CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="applications.csv"'
    writer = csv.writer(response)
    # Écrit l’en-tête
    writer.writerow(['nom', 'logo', 'utilisateur_id', 'cpu', 'ram', 'disk', 'services'])
    # Écrit les données
    for application in applications:
        writer.writerow([
            application.nom,
            application.logo,
            application.utilisateur_id,
            application.cpu,
            application.ram,
            application.disk,
            application.services
        ])
    return response