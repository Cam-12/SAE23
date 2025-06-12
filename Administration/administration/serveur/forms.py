from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
from django import forms

class typeServeurForm(ModelForm):
    class Meta:
        model = models.TypeServeurs
        fields = ('type', 'description')
        labels = {
            'type' : _('Type de serveur'),
            'description' : _('Description')
        }

class SeveursForm(ModelForm):
    class Meta:
        model = models.Serveurs
        fields = ('nom', 'type', 'cpu', 'ram', 'disk')
        labels = {
            'nom' : _('Nom du Serveur'),
            'type' : _("Le type de serveur"),
            'cpu' : _('Le nombre de processeurs'),
            'ram' : _('RAM'),
            'disk' : _('Stockage MAX')
        }

class ServicesForm(ModelForm):
    class Meta:
        model = models.Services
        fields = ('nom', 'date_lancement', 'ram_util', 'ram_ness', 'serveur_lanc', 'cpu', 'disk')
        labels = {
            'nom' : _('Nom du service'),
            'date_lancement' : _('Date de lancement'),
            'ram_util' : _('RAM utilisée'),
            'ram_ness' : _('RAM nécessaire'),
            'serveur_lanc' : _('Serveur de lancement'),
            'cpu': _('Nombres de processeurs'),
            'disk': _('Espace disque')
        }

    def clean(self):
        cleaned_data = super().clean()
        serveur = cleaned_data.get('serveur_lanc')
        ram_ness = cleaned_data.get('ram_ness')
        ram_util = cleaned_data.get('ram_util')
        cpu = cleaned_data.get('cpu')
        disk = cleaned_data.get('disk')

        if ram_util is not None and ram_ness is not None:
            if ram_util > ram_ness:
                self.add_error('ram_util', _("La RAM utilisée ne peut pas être supérieure à la RAM nécessaire."))

        if serveur:
            existing_services = models.Services.objects.filter(serveur_lanc=serveur)
            if self.instance.pk:
                existing_services = existing_services.exclude(pk=self.instance.pk)

            # --- RAM ---
            total_ram_ness = sum(s.ram_ness for s in existing_services) + (ram_ness or 0)
            if ram_ness is not None and total_ram_ness > serveur.ram:
                raise forms.ValidationError(
                    _(
                        "Ce serveur ne dispose plus de suffisamment de RAM.\n"
                        "RAM totale : %(total)s Go\n"
                        "RAM utilisée : %(utilisee)s Go\n"
                        "RAM demandée : %(demande)s Go"
                    ) % {
                        'total': serveur.ram,
                        'utilisee': total_ram_ness - ram_ness,
                        'demande': ram_ness
                    }
                )

            # --- CPU ---
            total_cpu = sum(s.cpu for s in existing_services) + (cpu or 0)
            if cpu is not None and total_cpu > serveur.cpu:
                raise forms.ValidationError(
                    _(
                        "Ce serveur ne dispose plus de suffisamment de CPU.\n"
                        "CPU total : %(total)s\n"
                        "CPU utilisé : %(utilise)s\n"
                        "CPU demandé : %(demande)s"
                    ) % {
                        'total': serveur.cpu,
                        'utilise': total_cpu - cpu,
                        'demande': cpu
                    }
                )

            # --- DISK ---
            total_disk = sum(s.disk for s in existing_services) + (disk or 0)
            if disk is not None and total_disk > serveur.disk:
                raise forms.ValidationError(
                    _(
                        "Ce serveur ne dispose plus de suffisamment d'espace disque.\n"
                        "Disque total : %(total)s Go\n"
                        "Disque utilisé : %(utilise)s Go\n"
                        "Disque demandé : %(demande)s Go"
                    ) % {
                        'total': serveur.disk,
                        'utilise': total_disk - disk,
                        'demande': disk
                    }
                )

        return cleaned_data

class ApplicationsForm(ModelForm):
    class Meta:
        model = models.Applications
        fields = ('nom', 'logo', 'utilisateur', 'cpu', 'ram', 'disk', 'service')
        labels = {
            'nom' : _("Nom de l'application"),
            'logo' : _("Logo de l'application"),
            'utilisateur' : _('Utilisateur associer'),
            'cpu': _('Nombres de processeurs'),
            'ram': _('RAM'),
            'disk': _('Espace disque'),
            'service': _('Service utilisée')
        }

    def clean(self):
        cleaned_data = super().clean()
        cpu = cleaned_data.get('cpu') or 0
        ram = cleaned_data.get('ram') or 0
        disk = cleaned_data.get('disk') or 0
        services = cleaned_data.get('service')

        if not services:
            return cleaned_data  # Aucun service sélectionné → aucune vérification possible

        for service in services:
            # Récupérer les autres applications déjà liées à ce service
            existing_apps = models.Applications.objects.filter(service=service)
            if self.instance.pk:
                existing_apps = existing_apps.exclude(pk=self.instance.pk)

            total_cpu = sum(app.cpu for app in existing_apps) + cpu
            total_ram = sum(app.ram for app in existing_apps) + ram
            total_disk = sum(app.disk for app in existing_apps) + disk

            # Vérification CPU
            if total_cpu > service.cpu:
                self.add_error('cpu', _(
                    f"Capacité CPU dépassée pour le service '{service.nom}'. "
                    f"Total demandé : {total_cpu} / Capacité : {service.cpu}"
                ))

            # Vérification RAM
            if total_ram > service.ram_util:
                self.add_error('ram', _(
                    f"Capacité RAM dépassée pour le service '{service.nom}'. "
                    f"Total demandé : {total_ram} / Capacité : {service.ram_util}"
                ))

            # Vérification disque
            if total_disk > service.disk:
                self.add_error('disk', _(
                    f"Capacité disque dépassée pour le service '{service.nom}'. "
                    f"Total demandé : {total_disk} / Capacité : {service.disk}"
                ))

        return cleaned_data
class UtilisateursForm(ModelForm):
    class Meta:
        model = models.Utilisateurs
        fields = ('nom', 'prenom', 'email')
        labels = {
            'nom' : _("Nom de l'utilisateur"),
            'prenom' : _("Prenom de l'utilisateur"),
            'email' : _("Email de l'utilisateur")
        }

class RessourcesForm(ModelForm):
    class Meta:
        model = models.Ressources
        fields = ('application', 'service')
        labels = {
            'application' : _("Nom de l'application"),
            'service' : _("Nom du service")
        }