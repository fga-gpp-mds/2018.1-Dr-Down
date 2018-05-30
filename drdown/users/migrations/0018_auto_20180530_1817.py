# Generated by Django 2.0.3 on 2018-05-30 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_remove_patient_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthteam',
            name='speciality',
            field=models.CharField(choices=[('Speech Therapy', 'Speech Therapy'), ('Psychology', 'Psychology'), ('Physiotherapy', 'Physiotherapy'), ('Occupational Therapy', 'Occupational Therapy'), ('General Practitioner', 'General Practitioner'), ('Cardiology', 'Cardiology'), ('Neurology', 'Neurology'), ('Pediatrics', 'Pediatrics'), ('Nursing', 'Nursing')], help_text='The speciality that this member of health team works.', max_length=30, verbose_name='Speciality'),
        ),
    ]