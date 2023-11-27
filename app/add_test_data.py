import os

import django
from faker import Faker

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "library.settings")
django.setup()

from app.travel_agency_app.models import City, Country

fake = Faker()


def generate_contacts_and_numbers(i=5, j=3):
    for _ in range(i):
        country = fake.country()
        country = Country.objects.update_or_create(name=country)
        for _ in range(j):
            city = fake.city()
            city = City.objects.update_or_create(name=city, country=country)
    print(f"Создано {j * i} городов и {i} стран")


if __name__ == "__main__":
    generate_contacts_and_numbers()

