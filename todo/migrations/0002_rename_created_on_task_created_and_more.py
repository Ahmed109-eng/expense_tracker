# Generated by Django 5.1.1 on 2024-09-24 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='created_on',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='Username',
            new_name='user',
        ),
    ]
