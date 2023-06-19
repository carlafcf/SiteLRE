# Generated by Django 4.1 on 2023-03-30 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Projeto', '0003_rename_descrição_projeto_descricao'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaPesquisa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=300, verbose_name='Nome')),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
            ],
        ),
        migrations.CreateModel(
            name='AreasPesquisaProjeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_pesquisa', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Projeto.areapesquisa')),
                ('projeto', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='Projeto.projeto')),
            ],
        ),
        migrations.AddField(
            model_name='projeto',
            name='areas_pesquisa',
            field=models.ManyToManyField(through='Projeto.AreasPesquisaProjeto', to='Projeto.areapesquisa'),
        ),
    ]
