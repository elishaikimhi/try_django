# Generated by Django 2.2 on 2019-11-21 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20191121_1435'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-publish_date', '-updated', '-time_stamp']},
        ),
    ]
