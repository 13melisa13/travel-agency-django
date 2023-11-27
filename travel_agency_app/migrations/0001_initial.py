# Generated by Django 4.2.6 on 2023-10-07 23:06

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('patronymic', models.CharField(blank=True, max_length=20, null=True)),
                ('phone_number', models.CharField(max_length=10)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time_start', models.DateTimeField()),
                ('duration', models.DurationField()),
                ('company', models.CharField(max_length=20)),
                ('city_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city_to', to='travel_agency_app.city')),
                ('city_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city_from', to='travel_agency_app.city')),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('stars_amount', models.IntegerField()),
                ('sea_distance', models.IntegerField(blank=True, null=True)),
                ('time_check_in', models.TimeField()),
                ('time_check_out', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': [('can_bought_tours', ''), ('can_view_own_tours', ''), ('can_view_own_contracts', '')],
            },
            bases=('travel_agency_app.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='TourAgency',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('commission_percent', models.IntegerField()),
            ],
            options={
                'permissions': [('can_add_contract', ''), ('can_update_contract', ''), ('can_view_own_contracts', '')],
            },
            bases=('travel_agency_app.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='TourOperator',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('commission_percent', models.IntegerField()),
            ],
            options={
                'permissions': [('can_add_tour', ''), ('can_update_own_tour', ''), ('can_disactivate_tour', ''), ('can_activate_tour', ''), ('can_view_own_saled_tour', '')],
            },
            bases=('travel_agency_app.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10000000)),
                ('dateFrom', models.DateTimeField()),
                ('dateTo', models.DateTimeField()),
                ('flight_from', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='flight_from', to='travel_agency_app.flight')),
                ('flight_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='flight_to', to='travel_agency_app.flight')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_agency_app.hotel')),
                ('tour_operator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='travel_agency_app.touroperator')),
            ],
        ),
        migrations.AddField(
            model_name='hotel',
            name='tags',
            field=models.ManyToManyField(to='travel_agency_app.tags'),
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_agency_app.country'),
        ),
        migrations.AddField(
            model_name='city',
            name='tags',
            field=models.ManyToManyField(to='travel_agency_app.tags'),
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=256)),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_agency_app.tour')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel_agency_app.client')),
                ('tour_agency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='travel_agency_app.touragency')),
            ],
        ),
    ]
