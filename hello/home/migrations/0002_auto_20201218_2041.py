# Generated by Django 3.1.3 on 2020-12-18 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='Message',
            new_name='message',
        ),
    ]
