# Generated by Django 5.0.2 on 2024-02-26 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='descripction',
            new_name='description',
        ),
    ]