from django.core.management.base import BaseCommand
from inicio.models import Configuracion



class Command(BaseCommand):
    help = 'Crea 5 registros de configuracion'

    def handle(self, *args, **kwargs):
        # Crear una lista de datos para los hoteles
        configuracion_data = [
           {'dato': 'telefono_1', 'valor': '17340458'},
            {'dato': 'telefono_2', 'valor': '27340458'},
            {'dato': 'facebook', 'valor': 'https://facebook.com'},
            {'dato': 'instagram', 'valor': 'https://instagram.com'},
            {'dato': 'email_admin', 'valor': 'demo@demo.cl'},
        ]
        
        # Iterar sobre los datos y crear registros en la base de datos
        for data in configuracion_data:
            Configuracion.objects.create(**data)
        
        self.stdout.write(self.style.SUCCESS('5 registros creados de configuracion'))

