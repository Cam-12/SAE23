import json
from django.core.management.base import BaseCommand
from serveur.models import Serveurs, TypeServeurs


class Command(BaseCommand):
    help = 'Importe des serveurs avec leur type depuis un fichier JSON'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Chemin vers le fichier JSON')

    def handle(self, *args, **kwargs):
        json_file = kwargs['json_file']

        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Erreur de lecture du fichier JSON : {e}"))
            return

        for item in data:
            try:
                type_nom = item['type']
                type_obj, _ = TypeServeurs.objects.get_or_create(
                    type=type_nom,
                    defaults={'description': f"Type généré automatiquement : {type_nom}"}
                )

                serveur, created = Serveurs.objects.get_or_create(
                    nom=item['nom'],
                    defaults={
                        'type': type_obj,
                        'cpu': item['cpu'],
                        'ram': item['ram'],
                        'disk': item['disk']
                    }
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f"Serveur ajouté : {serveur.nom}"))
                else:
                    self.stdout.write(self.style.WARNING(f"Serveur existant ignoré : {serveur.nom}"))

            except KeyError as ke:
                self.stderr.write(self.style.ERROR(f"Champ manquant : {ke} dans l'entrée : {item}"))
            except Exception as e:
                self.stderr.write(
                    self.style.ERROR(f"Erreur lors de l'import du serveur {item.get('nom', 'Inconnu')} : {e}"))
