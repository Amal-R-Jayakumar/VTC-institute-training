# Generated by Django 3.2.8 on 2021-11-05 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vtc_exact_app', '0003_batch'),
        ('courses', '0002_enrollment_testquestion'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='batch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vtc_exact_app.batch'),
        ),
    ]