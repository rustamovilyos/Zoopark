# Generated by Django 3.2.9 on 2021-11-05 00:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0009_auto_20211105_0003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='caretaker',
            old_name='name',
            new_name='name_is',
        ),
        migrations.RenameField(
            model_name='pet',
            old_name='name',
            new_name='pseudonym',
        ),
    ]
