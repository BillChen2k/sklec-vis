# Generated by Django 4.0.2 on 2022-03-18 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_remove_datachannel_is_xaxis_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='datachannel',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
