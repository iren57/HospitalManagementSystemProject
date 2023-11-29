# Generated by Django 4.2.7 on 2023-11-26 04:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0004_alter_patient_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='patient',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='patient.patient'),
        ),
        migrations.AlterField(
            model_name='medicalhistory',
            name='patient',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='patient.patient'),
        ),
    ]