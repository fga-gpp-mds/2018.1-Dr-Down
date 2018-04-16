# Generated by Django 2.0.3 on 2018-04-16 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20180416_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='health_team',
            name='state_register',
            field=models.CharField(blank=True, choices=[(('Acre',), 'Acre'), (('Alagoas',), 'Alagoas'), (('Amapá',), 'Amapá'), (('Bahia',), 'Bahia'), (('Ceará',), 'Ceará'), (('Distrito Federal',), 'Distrito Federal'), (('Espírito Santo',), 'Espírito Santo'), (('Goiás',), 'Goiás'), (('Maranhão',), 'Maranão'), (('Minas Gerais',), 'Minas Gerais'), (('Mato Grosso do Sul',), 'Mato Grosso do Sul'), (('Mato Grosso',), 'Mato Grosso'), (('Pará',), 'Pará'), (('Paraíba',), 'Paraíba'), (('Pernanbuco',), 'Pernanbuco'), (('Piauí',), 'Piauí'), (('Paraná',), 'Paraná'), (('Rio de Janeiro',), 'Rio de Janeiro'), (('Rio Grande do Norte',), 'Rio Grande do Norte'), (('Rondônia',), 'Rondônia'), (('Roraima',), 'Roraima'), (('Rio Grande do Sul',), 'Rio Grande do Sul'), (('Santa Catarina',), 'Santa Catarina'), (('Sergipe',), 'Sergipe'), (('São Paulo',), 'São Paulo'), ('Tocantins', 'Tocantins')], help_text='The state of register health team member works.', max_length=30, verbose_name='State'),
        ),
    ]