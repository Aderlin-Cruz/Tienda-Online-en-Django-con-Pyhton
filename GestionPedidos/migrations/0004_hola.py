# Generated by Django 3.1.5 on 2021-01-14 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GestionPedidos', '0003_auto_20210110_2159'),
    ]

    operations = [
        migrations.CreateModel(
            name='hola',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entregado', models.BooleanField()),
            ],
        ),
    ]
