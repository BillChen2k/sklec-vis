# Generated by Django 4.0.2 on 2022-04-06 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_alter_datachannel_uuid_alter_dataset_uuid_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='visfile',
            options={'ordering': ['datetime_start', 'file_name']},
        ),
    ]
