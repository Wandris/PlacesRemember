# Generated by Django 3.1.4 on 2020-12-21 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0008_auto_20201221_0659'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mymodel',
            old_name='field1',
            new_name='feelings',
        ),
        migrations.RemoveField(
            model_name='mymodel',
            name='field2',
        ),
        migrations.RemoveField(
            model_name='mymodel',
            name='field3',
        ),
    ]