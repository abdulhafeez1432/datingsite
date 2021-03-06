# Generated by Django 3.2.4 on 2021-06-27 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_auto_20210627_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='religion',
            name='imam',
            field=models.CharField(default=1, max_length=150, verbose_name='The Name of Imam where you Pray'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='religion',
            name='imam_phone_number',
            field=models.CharField(choices=[('Al-Sunnah', 'Al-Sunnah'), ('Salafi', 'Salafi')], default=1, max_length=150, verbose_name='Your Imam Phone Number'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='religion',
            name='program',
            field=models.CharField(default=1, max_length=150, verbose_name='Which Program Do you Attend'),
            preserve_default=False,
        ),
    ]
