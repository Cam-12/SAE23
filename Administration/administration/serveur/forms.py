from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

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
        fields = ('nom', 'date_lancement', 'ram_util', 'ram_ness', 'serveur_lanc')
        labels = {
            'nom' : _('Nom du service'),
            'date_lancement' : _('Date de lancement'),
            'ram_util' : _('RAM utilisée'),
            'ram_ness' : _('RAM nécessaire'),
            'serveur_lanc' : _('Serveur de lancement')
        }

class ApplicationsForm(ModelForm):
    class Meta:
        model = models.Applications
        fields = ('nom', 'logo', 'utilisateur')
        labels = {
            'nom' : _("Nom de l'application"),
            'logo' : _("Logo de l'application"),
            'utilisateur' : _('Utilisateur associer')
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