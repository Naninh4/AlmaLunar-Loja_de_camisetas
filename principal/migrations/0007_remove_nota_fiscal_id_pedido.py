# Generated by Django 4.1.4 on 2022-12-28 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0006_alter_nota_fiscal_id_adress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nota_fiscal',
            name='id_pedido',
        ),
    ]
