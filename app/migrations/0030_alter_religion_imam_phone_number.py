# Generated by Django 3.2.4 on 2021-06-27 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_auto_20210627_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='religion',
            name='imam_phone_number',
            field=models.CharField(help_text='+23410938846', max_length=15, verbose_name='Your Imam Phone Number'),
        ),
    ]