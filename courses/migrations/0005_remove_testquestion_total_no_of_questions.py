# Generated by Django 3.2.8 on 2021-11-06 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_testquestion_total_no_of_questions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testquestion',
            name='total_no_of_questions',
        ),
    ]
