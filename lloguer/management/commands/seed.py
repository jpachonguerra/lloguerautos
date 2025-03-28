from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker
import random
from datetime import timedelta, date
from lloguer.models import *

fake = Faker()

class Command(BaseCommand):
    help = 'Seed database with sample data'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Seeding database...'))
        
        # Crear automóviles
        automobils = list(Automobil.objects.all())
        for _ in range(4):
            automobil = Automobil.objects.create(
                marca=fake.company(),
                model=fake.word(),
                matricula=fake.unique.license_plate()
            )
            automobils.append(automobil)

        # Crear usuarios
        users = list(User.objects.all())
        for _ in range(8):
            user = User.objects.create_user(
                username=fake.unique.user_name(),
                email=fake.email(),
                password='password123'
            )
            users.append(user)

        # Crear reservas (entre 1 y 2 por usuario)
        for user in users:
            num_reservas = random.randint(1, 2)
            for _ in range(num_reservas):
                automobil = random.choice(automobils)
                data_inici = fake.date_between(start_date='-30d', end_date='+30d')
                data_final = data_inici + timedelta(days=random.randint(1, 7))
                
                if not Reserva.objects.filter(automobil=automobil, data_inici=data_inici).exists():
                    Reserva.objects.create(
                        automobil=automobil,
                        usuari=user,
                        data_inici=data_inici,
                        data_final=data_final
                    )
        
        self.stdout.write(self.style.SUCCESS('Database seeding complete!'))