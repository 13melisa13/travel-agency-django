from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Country(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def get_absolute_url(self):
        return reverse('country-detail', args=[str(self.id)])


class Tags(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=256)


class City(models.Model):
    name = models.CharField(max_length=20)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tags)

    def get_absolute_url(self):
        return reverse('city-detail', args=[str(self.id)])


class Hotel(models.Model):
    name = models.CharField(max_length=20)
    stars_amount = models.IntegerField()
    sea_distance = models.IntegerField(blank=True, null=True)
    time_check_in = models.TimeField()
    time_check_out = models.TimeField()
    tags = models.ManyToManyField(Tags)

    def get_absolute_url(self):
        return reverse('hotel-detail', args=[str(self.id)])


class User(AbstractUser):
    # name = models.CharField(max_length=20) name
    # surname = models.CharField(max_length=20) last_name
    patronymic = models.CharField(max_length=20, blank=True, null=True)
    # email = models.EmailField(max_length=40, unique=True) username
    # password = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=10)


class TourOperator(User):
    commission_percent = models.IntegerField()
    # TODO calc_commission

    class Meta:
        permissions = [
            ("can_add_tour", ""),
            ("can_update_own_tour", ""),
            ("can_disactivate_tour", ""),
            ("can_activate_tour", ""),
            ("can_view_own_saled_tour", "")
        ]


class TourAgency(User):
    commission_percent = models.IntegerField()
    # TODO calc_commission

    class Meta:
        permissions = [
            ("can_add_contract", ""),
            ("can_update_contract", ""),
            ("can_view_own_contracts", "")
        ]


class Client(User):
    passport = models.CharField(max_length=10)
    # необязятельно вводить password, username
    class Meta:
        permissions = [
            ("can_bought_tours", ""),
            ("can_view_own_tours", ""),
            ("can_view_own_contracts", "")
        ]


class Flight(models.Model):
    city_from = models.ForeignKey(City, on_delete=models.CASCADE, related_name="city_to")
    # time_zone from city
    city_to = models.ForeignKey(City, on_delete=models.CASCADE,  related_name="city_from")
    date_time_start = models.DateTimeField()
    duration = models.DurationField()
    company = models.CharField(max_length=20)
    # get from api date_time_finish time_zone


class Tour(models.Model):
    price = models.DecimalField(decimal_places=2, max_digits=10000000)
    dateFrom = models.DateTimeField()
    dateTo = models.DateTimeField()
    flight_to = models.ForeignKey(Flight, on_delete=models.SET_NULL, blank=True, null=True, related_name="flight_to")
    flight_from = models.ForeignKey(Flight, on_delete=models.SET_NULL, blank=True, null=True, related_name="flight_from")
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    tour_operator = models.ForeignKey(TourOperator, null=True, blank=True, on_delete=models.CASCADE)
#    custom tour created by clients like internet shop


class Contract(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    tour_agency = models.ForeignKey(TourAgency, null=True, blank=True, on_delete=models.CASCADE)
    #    custom contract created by clients like internet shop
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    # contract = models.TextField(max_length=512)
    link = models.CharField(max_length=256)




