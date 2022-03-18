# Generated by Django 4.0.2 on 2022-03-16 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_datachannels_unit_symbol_datachannels_uuid_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visfile',
            old_name='georeinforced',
            new_name='is_georeferenced',
        ),
        migrations.AddField(
            model_name='rawfile',
            name='folder_hierarchy',
            field=models.CharField(blank=True, default='/', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='rawfile',
            name='meta_data',
            field=models.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='visfile',
            name='meta_data',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='datachannels',
            name='shape',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]