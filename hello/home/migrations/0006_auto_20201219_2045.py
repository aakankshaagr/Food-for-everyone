# Generated by Django 3.1.3 on 2020-12-19 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_contact_entrydate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='message',
            new_name='message1',
        ),
    ]
