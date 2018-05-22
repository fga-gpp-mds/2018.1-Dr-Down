# Generated by Django 2.0.3 on 2018-05-21 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_remove_patient_priority'),
        ('medicalrecords', '0007_auto_20180520_1645'),
    ]

    operations = [
        migrations.CreateModel(
            name='Risk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority_speech_theraphy', models.IntegerField(choices=[(5, 'Not urgent'), (4, 'Not very urgent'), (3, 'Urgent'), (2, 'Very urgent'), (1, 'Emerging')], help_text='Please, insert the degree of speech therapy priority of the patient', verbose_name='Speech Therapy Priority')),
                ('priority_psychology', models.IntegerField(choices=[(5, 'Not urgent'), (4, 'Not very urgent'), (3, 'Urgent'), (2, 'Very urgent'), (1, 'Emerging')], help_text='Please, insert the degree of psychology priority of the patient', verbose_name='Psychology Priority')),
                ('priority_physiotherapy', models.IntegerField(choices=[(5, 'Not urgent'), (4, 'Not very urgent'), (3, 'Urgent'), (2, 'Very urgent'), (1, 'Emerging')], help_text='Please, insert the degree of physiotherapy priority of the patient', verbose_name='Physiotherapy Priority')),
                ('priority_cardiology', models.IntegerField(choices=[(5, 'Not urgent'), (4, 'Not very urgent'), (3, 'Urgent'), (2, 'Very urgent'), (1, 'Emerging')], help_text='Please, insert the degree of cardiology priority of the patient', verbose_name='Cardiology Priority')),
                ('priority_neurology', models.IntegerField(choices=[(5, 'Not urgent'), (4, 'Not very urgent'), (3, 'Urgent'), (2, 'Very urgent'), (1, 'Emerging')], help_text='Please, insert the degree of neurology priority of the patient', verbose_name='Neurology Priority')),
                ('priority_pediatrics', models.IntegerField(choices=[(5, 'Not urgent'), (4, 'Not very urgent'), (3, 'Urgent'), (2, 'Very urgent'), (1, 'Emerging')], help_text='Please, insert the degree of pediatrics priority of the patient', verbose_name='Pediatrics Priority')),
                ('priority_general_practitioner', models.IntegerField(choices=[(5, 'Not urgent'), (4, 'Not very urgent'), (3, 'Urgent'), (2, 'Very urgent'), (1, 'Emerging')], help_text='Please, insert the degree of general practitioner priority of the patient', verbose_name='Nursing Priority')),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.Patient', verbose_name='Patient')),
            ],
        ),
    ]