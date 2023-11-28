from faker import Faker
from .models import City, Country


def generate_contacts_and_numbers(i=5, j=3):
    fake = Faker()

    for _ in range(i):
        country = fake.country()
        country = Country.objects.update_or_create(name=country)
        for _ in range(j):
            city = fake.city()
            city = City.objects.update_or_create(name=city, country=country)
    print(f"Создано {j * i} городов и {i} стран")


generate_contacts_and_numbers(2, 2)
