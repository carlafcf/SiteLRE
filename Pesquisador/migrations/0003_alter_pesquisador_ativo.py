# Generated by Django 4.1 on 2023-03-15 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pesquisador', '0002_rename_status_pesquisador_ativo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pesquisador',
            name='ativo',
            field=models.BooleanField(default=True, verbose_name='Ativo'),
        ),
    ]
