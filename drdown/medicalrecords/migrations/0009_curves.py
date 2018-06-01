# Generated by Django 2.0.3 on 2018-06-01 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_remove_patient_priority'),
        ('medicalrecords', '0008_risk'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curves',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField(default=0.0)),
                ('height', models.IntegerField(default=0)),
                ('cephalic_perimeter', models.FloatField(default=0.0)),
                ('bmi', models.FloatField(default=0.0)),
                ('age', models.IntegerField(default=0)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Patient', verbose_name='Patient')),
            ],
        ),
    ]