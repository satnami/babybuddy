# Generated by Django 2.2.2 on 2019-06-18 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0005_auto_20190602_1233'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='medicationrecurrence',
            options={'default_permissions': ('view', 'add', 'change', 'delete'), 'ordering': ['-start'], 'verbose_name': 'Medication schedule', 'verbose_name_plural': 'Medication schedules'},
        ),
        migrations.AddField(
            model_name='medicationrecurrence',
            name='complete',
            field=models.BooleanField(default=False, verbose_name='Complete'),
        ),
    ]