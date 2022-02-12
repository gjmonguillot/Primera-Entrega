# Generated by Django 4.0.2 on 2022-02-11 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tipo_de_Carrera', models.CharField(max_length=40)),
                ('Superficie', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Corredor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('edad', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Indumentaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talle_remera', models.CharField(max_length=3)),
                ('talle_zapatillas', models.IntegerField()),
            ],
        ),
    ]
