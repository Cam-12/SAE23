from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # TypeServeur URLs
    path('type_serveur/', views.list_type_serveur, name='list_type_serveur'),
    path('type_serveur/add/', views.add_type_serveur, name='add_type_serveur'),
    path('type_serveur/update/<int:id>/', views.update_type_serveur, name='update_type_serveur'),
    path('type_serveur/delete/<int:id>/', views.delete_type_serveur, name='delete_type_serveur'),

    # Serveur URLs
    path('serveur/', views.list_serveurs, name='list_serveurs'),
    path('serveur/add/', views.add_serveur, name='add_serveur'),
    path('serveur/update/<int:id>/', views.update_serveur, name='update_serveur'),
    path('serveur/delete/<int:id>/', views.delete_serveur, name='delete_serveur'),

    # Service URLs
    path('service/', views.list_services, name='list_services'),
    path('service/add/', views.add_service, name='add_service'),
    path('service/update/<int:id>/', views.update_service, name='update_service'),
    path('service/delete/<int:id>/', views.delete_service, name='delete_service'),

    # Utilisateur URLs
    path('utilisateur/', views.list_utilisateurs, name='list_utilisateurs'),
    path('utilisateur/add/', views.add_utilisateur, name='add_utilisateur'),
    path('utilisateur/update/<int:id>/', views.update_utilisateur, name='update_utilisateur'),
    path('utilisateur/delete/<int:id>/', views.delete_utilisateur, name='delete_utilisateur'),

    # Application URLs
    path('application/', views.list_applications, name='list_applications'),
    path('application/add/', views.add_application, name='add_application'),
    path('application/update/<int:id>/', views.update_application, name='update_application'),
    path('application/delete/<int:id>/', views.delete_application, name='delete_application'),

    # UsageRessource URLs
    path('usageressource/', views.list_usageressources, name='list_usageressources'),
    path('usageressource/add/', views.add_usageressource, name='add_usageressource'),
    path('usageressource/update/<int:id>/', views.update_usageressource, name='update_usageressource'),
    path('usageressource/delete/<int:id>/', views.delete_usageressource, name='delete_usageressource'),

    path('serveur/import_serveur/', views.import_serveur, name='import_serveur'),
    path('serveur/import_type_serveur/', views.import_type_serveur, name='import_type_serveur'),
    path('serveur/import_service/', views.import_service, name='import_service'),
    path('serveur/import_utilisateur/', views.import_utilisateur, name='import_utilisateur'),
    path('serveur/import_application/', views.import_application, name='import_application'),

    path('serveur/export_serveurs/', views.export_serveurs_csv, name='export_serveurs_csv'),
    path('serveur/export_type_serveurs/', views.export_type_serveurs_csv, name='export_type_serveurs_csv'),
    path('serveur/export_services/', views.export_services_csv, name='export_services_csv'),
    path('serveur/export_utilisateurs/', views.export_utilisateurs_csv, name='export_utilisateurs_csv'),
    path('serveur/export_applications/', views.export_applications_csv, name='export_applications_csv'),
]
