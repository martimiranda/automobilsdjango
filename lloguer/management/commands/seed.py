

import random,datetime
from datetime import datetime, timedelta
from faker import Faker
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from lloguer.models import *

fake = Faker('es_ES')




class Command(BaseCommand):
    help = 'Seed database with initial data'


    def handle(self, *args, **kwargs):
        create_automobil()


def create_automobil():
    
    for _ in range(100):
            marca = fake.word()
            model = fake.word() 
            matricula = fake.license_plate()

            Automobil.objects.create(marca=marca, model=model, matricula=matricula)