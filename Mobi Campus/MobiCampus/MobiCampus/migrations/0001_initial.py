# Generated by Django 4.1 on 2022-09-24 23:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Carona',
            fields=[
                ('caronaId', models.AutoField(primary_key=True, serialize=False)),
                ('origem', models.CharField(max_length=50)),
                ('tempo', models.IntegerField()),
                ('destino', models.CharField(max_length=50)),
                ('rota', models.CharField(max_length=300)),
                ('custo', models.IntegerField()),
                ('finalizada', models.BooleanField(default=False)),
                ('passageiros', models.SmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aval', models.SmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=5)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MobiCampus.usuario')),
                ('permissao', models.BooleanField()),
            ],
            bases=('MobiCampus.usuario',),
        ),
        migrations.CreateModel(
            name='Motorista',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='MobiCampus.usuario')),
                ('cnh', models.CharField(max_length=11)),
            ],
            bases=('MobiCampus.usuario',),
        ),
        migrations.CreateModel(
            name='CaronaHist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=10)),
                ('carona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MobiCampus.carona')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to='MobiCampus.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Solicitacao',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Aceito', models.BooleanField(default=False)),
                ('Carona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MobiCampus.carona')),
                ('Passageiro', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Passageiro', to='MobiCampus.usuario')),
                ('Motorista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Motorista', to='MobiCampus.motorista')),
            ],
        ),
        migrations.AddField(
            model_name='carona',
            name='motorista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MobiCampus.motorista'),
        ),
    ]
