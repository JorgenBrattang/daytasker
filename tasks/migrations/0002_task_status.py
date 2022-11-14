# Generated by Django 3.2.16 on 2022-11-14 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(blank=True, choices=[('not_done', 'Not Done'), ('in_progress', 'In Progress'), ('done', 'Done')], max_length=50, null=True),
        ),
    ]