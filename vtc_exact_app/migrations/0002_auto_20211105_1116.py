# Generated by Django 3.2.8 on 2021-11-05 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vtc_exact_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vtcmodel',
            name='category',
        ),
        migrations.RemoveField(
            model_name='vtcmodel',
            name='course',
        ),
    ]
