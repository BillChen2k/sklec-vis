# Generated by Django 4.0.2 on 2022-03-16 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_datachannel_alter_downloadrecord_dataset_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datachannel',
            name='visfile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data_channels', to='api.visfile'),
        ),
    ]
