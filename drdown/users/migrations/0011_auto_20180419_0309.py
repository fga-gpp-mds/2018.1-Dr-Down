# Generated by Django 2.0.3 on 2018-04-19 03:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_merge_20180419_0308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='user',
            field=models.OneToOneField(limit_choices_to=models.Q(has_specialization=False), on_delete=django.db.models.deletion.CASCADE, related_name='patient', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
