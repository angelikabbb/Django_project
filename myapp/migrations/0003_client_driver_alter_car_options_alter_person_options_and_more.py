# Generated by Django 4.2.2 on 2023-06-22 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_car'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('birthday', models.DateField(verbose_name='Дата рождения')),
                ('age', models.IntegerField(null=True, verbose_name='Возраст')),
                ('city', models.CharField(max_length=30, verbose_name='Город')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254, verbose_name='Эл. почта')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('age', models.IntegerField(null=True, verbose_name='Возраст')),
                ('experience', models.IntegerField(verbose_name='Опыт работы')),
                ('phone', models.CharField(max_length=30, verbose_name='Телефон')),
                ('workplace', models.CharField(max_length=50, verbose_name='Предыдущее место работы')),
            ],
            options={
                'verbose_name': 'Водитель',
                'verbose_name_plural': 'Водители',
            },
        ),
        migrations.AlterModelOptions(
            name='car',
            options={'verbose_name': 'Mashina', 'verbose_name_plural': 'Mashiny'},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Человек', 'verbose_name_plural': 'Люди'},
        ),
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.CharField(max_length=30, verbose_name='Марка'),
        ),
        migrations.AlterField(
            model_name='car',
            name='color',
            field=models.CharField(max_length=30, verbose_name='Цвет'),
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(max_length=30, verbose_name='Модель'),
        ),
        migrations.AlterField(
            model_name='car',
            name='power',
            field=models.IntegerField(verbose_name='Мощность'),
        ),
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.IntegerField(verbose_name='Год выпуска'),
        ),
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.IntegerField(verbose_name='age'),
        ),
        migrations.AlterField(
            model_name='person',
            name='city',
            field=models.CharField(max_length=100, verbose_name='city'),
        ),
        migrations.AlterField(
            model_name='person',
            name='is_activated',
            field=models.BooleanField(verbose_name='activation'),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=100, verbose_name='name'),
        ),
    ]
