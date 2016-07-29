# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-28 12:35
from __future__ import unicode_literals

from django.db import migrations, models
import two_digits.models

def add_data(apps, schema_editor):
    Digit = apps.get_model("two_digits", "Digitview")
    for n in range(0,100):#Digit.objects.all():
        Digit.add(digit=n, word='').save()

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DigitAssoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('digit', models.CharField(max_length=2, unique=True, verbose_name='Число')),
                ('word', models.CharField(max_length=100, verbose_name='Ассоциация')),
                ('foto', models.ImageField(upload_to=two_digits.models.DigitAssoc.get_user_filename)),
            ],
        ),
        migrations.RunPython(add_data),
    ]