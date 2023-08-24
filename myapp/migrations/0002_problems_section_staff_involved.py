# Generated by Django 4.2.4 on 2023-08-18 08:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='problems_section',
            name='staff_involved',
            field=models.ManyToManyField(limit_choices_to={'staff_is': True}, related_name='staff_involved_problems', to=settings.AUTH_USER_MODEL),
        ),
    ]