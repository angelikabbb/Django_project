# Generated by Django 4.2.2 on 2023-06-24 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_client_driver_alter_car_options_alter_person_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50, verbose_name='Имя')),
                ('lastname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('birthday', models.DateField(verbose_name='Дата рождения')),
                ('position', models.CharField(max_length=50, verbose_name='Должность')),
                ('education', models.CharField(choices=[('middle', 'среднее'), ('high', 'высшее'), ('professional', 'профессиональное')], max_length=50)),
            ],
        ),
        migrations.AlterModelOptions(
            name='car',
            options={'verbose_name': 'Машина', 'verbose_name_plural': 'Машины'},
        ),
    ]