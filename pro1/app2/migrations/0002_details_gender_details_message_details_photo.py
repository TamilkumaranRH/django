# Generated by Django 5.0.6 on 2024-07-01 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='details',
            name='gender',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='details',
            name='message',
            field=models.CharField(blank=True, max_length=4096, null=True),
        ),
        migrations.AddField(
            model_name='details',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
