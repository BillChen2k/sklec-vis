# Generated by Django 4.0.2 on 2022-04-05 10:16

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_alter_datachannel_uuid_alter_dataset_uuid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datachannel',
            name='uuid',
            field=models.CharField(default=api.models.uuid4_short, editable=False, max_length=20),
        ),
        migrations.AlterField(
            model_name='dataset',
            name='uuid',
            field=models.CharField(default=api.models.uuid4_short, editable=False, max_length=20),
        ),
        migrations.AlterField(
            model_name='datasettag',
            name='uuid',
            field=models.CharField(default=api.models.uuid4_short, editable=False, max_length=20),
        ),
        migrations.AlterField(
            model_name='rawfile',
            name='uuid',
            field=models.CharField(default=api.models.uuid4_short, editable=False, max_length=20),
        ),
        migrations.AlterField(
            model_name='siteuser',
            name='uuid',
            field=models.CharField(default=api.models.uuid4_short, editable=False, max_length=20),
        ),
        migrations.AlterField(
            model_name='visfile',
            name='uuid',
            field=models.CharField(default=api.models.uuid4_short, editable=False, max_length=20),
        ),
    ]