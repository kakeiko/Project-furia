# Generated by Django 5.2 on 2025-04-27 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fanprofile', '0005_remove_fanprofile_nivel_engajamento'),
    ]

    operations = [
        migrations.AddField(
            model_name='fanprofile',
            name='tweets_relacionados',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
