from django.db import models
from django.core.exceptions import ValidationError

class TypeServeurs(models.Model):
    type = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=100, blank=False)

    def __str__(self):
        chaine = f"{self.type}"
        return chaine

    def dicoTypeServeurs(self):
        return {"type": self.type, "description": self.description}

class Serveurs(models.Model):
    nom = models.CharField(max_length=100, blank=False)
    type = models.ForeignKey(TypeServeurs, on_delete=models.CASCADE)
    cpu = models.IntegerField(blank=False)
    ram = models.IntegerField(blank=False)
    disk = models.IntegerField(blank=False)

    def __str__(self):
        chaine = f"{self.nom}"
        return chaine

    def dicoServeurs(self):
        return {"nom": self.nom, "type": self.type, "cpu": self.cpu, "ram": self.ram, "disk": self.disk}

class Services(models.Model):
    nom = models.CharField(max_length=100, blank=False)
    date_lancement = models.DateField(blank=False)
    ram_util = models.IntegerField(blank=False)
    ram_ness = models.IntegerField(blank=False)
    serveur_lanc = models.ForeignKey(Serveurs, on_delete=models.CASCADE)
    cpu = models.IntegerField(blank=False, default=1)
    disk = models.IntegerField(blank=False, default=1)

    def __str__(self):
        chaine = f"{self.nom}"
        return chaine

    def dicoServices(self):
        return {"nom": self.nom, "date_lancement": self.date_lancement, "ram_util": self.ram_util, "ram_ness": self.ram_ness, "serveur_lanc": self.serveur_lanc, "cpu": self.cpu, "disk": self.disk}



class Utilisateurs(models.Model):
    nom = models.CharField(max_length=100, blank=False)
    prenom = models.CharField(blank=False)
    email = models.CharField(blank=False)

    def __str__(self):
        chaine = f"{self.nom}"
        return chaine

    def dicoUtilisateurs(self):
        return {"nom": self.nom, "prenom": self.prenom, "email": self.email}

class Applications(models.Model):
    nom = models.CharField(max_length=100, blank=False)
    logo = models.ImageField(upload_to='logos/', null=True, blank=False)
    utilisateur = models.ForeignKey('Utilisateurs', on_delete=models.CASCADE)
    cpu = models.IntegerField(blank=False, default=1)
    ram = models.IntegerField(blank=False, default=1)
    disk = models.IntegerField(blank=False, default=1)
    service = models.ManyToManyField(Services, through='Ressources')

    def __str__(self):
        chaine = f"{self.nom}"
        return chaine

    def dicoApplications(self):
        return {"nom": self.nom, "logo": self.logo, "utilisateur": self.utilisateur, "cpu": self.cpu, "ram": self.ram, "disk": self.disk, "service": self.service}

class Ressources(models.Model):
    application = models.ForeignKey(Applications, on_delete=models.CASCADE)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)

    def __str__(self):
        chaine = f"{self.application}"
        return chaine

    def dicoRessources(self):
        return {"application": self.application, "service": self.service}