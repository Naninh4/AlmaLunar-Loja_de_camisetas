# Generated by Django 4.1.4 on 2022-12-18 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0012_remove_cliente_id_endereco_delete_endereco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='pais',
            field=models.CharField(max_length=20),
        ),
    ]
