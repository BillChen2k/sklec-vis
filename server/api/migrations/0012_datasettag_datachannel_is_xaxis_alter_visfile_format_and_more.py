# Generated by Django 4.0.2 on 2022-03-17 08:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_datachannel_visfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatasetTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('long_name', models.CharField(blank=True, max_length=100, null=True)),
                ('fa_icon', models.CharField(blank=True, max_length=50, null=True)),
                ('color', models.CharField(blank=True, max_length=20, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='datachannel',
            name='is_xaxis',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='visfile',
            name='format',
            field=models.CharField(choices=[('rsk', 'Rsk'), ('csv', 'Csv'), ('ncf', 'Ncf'), ('tiff', 'Tiff'), ('other', 'Other')], default='other', max_length=20),
        ),
        migrations.AddField(
            model_name='dataset',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='api.DatasetTag'),
        ),
    ]
