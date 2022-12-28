# Generated by Django 4.1.4 on 2022-12-28 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0003_delete_adress'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_cliente', models.IntegerField()),
                ('pais', models.CharField(max_length=200)),
                ('estado', models.CharField(max_length=200)),
                ('cidade', models.CharField(max_length=200)),
                ('bairro', models.CharField(max_length=200)),
                ('rua', models.CharField(max_length=200)),
                ('numero', models.IntegerField()),
            ],
        ),
    ]
