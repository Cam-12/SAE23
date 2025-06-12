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

        # 1. Vérifier que RAM utilisée ≤ RAM nécessaire
        if ram_util is not None and ram_ness is not None:
            if ram_util > ram_ness:
                self.add_error('ram_util', _("La RAM utilisée ne peut pas être supérieure à la RAM nécessaire."))

        # 2. Vérifier que la RAM totale demandée ne dépasse pas la RAM du serveur
        if serveur and ram_ness is not None:
            existing_services = models.Services.objects.filter(serveur_lanc=serveur)
            if self.instance.pk:
                existing_services = existing_services.exclude(pk=self.instance.pk)

            ram_necessaire_actuelle = sum(service.ram_ness for service in existing_services)
            ram_necessaire_totale = ram_necessaire_actuelle + ram_ness

            if ram_necessaire_totale > serveur.ram:
                raise forms.ValidationError(
                    _(
                        "Ce serveur ne dispose plus de suffisamment de RAM.\n"
                        "RAM disponible : %(ram_total)s Go\n"
                        "RAM déjà utilisée : %(ram_utilisee)s Go\n"
                        "RAM demandée : %(ram_nouvelle)s Go\n"
                        "RAM totale après ajout : %(ram_totale)s Go"
                    ) % {
                        'ram_total': serveur.ram,
                        'ram_utilisee': ram_necessaire_actuelle,
                        'ram_nouvelle': ram_ness,
                        'ram_totale': ram_necessaire_totale
                    }
                )

        return cleaned_data

class ApplicationsForm(ModelForm):
    class Meta:
        model = models.Applications
        fields = ('nom', 'logo', 'utilisateur', 'cpu', 'ram', 'disk')
        labels = {
            'nom' : _("Nom de l'application"),
            'logo' : _("Logo de l'application"),
            'utilisateur' : _('Utilisateur associer'),
            'cpu': _('Nombres de processeurs'),
            'ram': _('RAM'),
            'disk': _('Espace disque')
        }

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