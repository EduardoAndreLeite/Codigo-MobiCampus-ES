# Generated by Django 4.1 on 2022-09-06 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MobiCampus', '0002_alter_carona_motorista'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caronaaux',
            name='passageiro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='passageiro', to='MobiCampus.usuario'),
        ),
    ]