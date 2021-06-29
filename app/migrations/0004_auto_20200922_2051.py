# Generated by Django 3.1.1 on 2020-09-22 19:51

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='mention_challenges',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='If, Yes, Mention the form of Disability'),
        ),
        migrations.AlterField(
            model_name='family',
            name='brother',
            field=models.PositiveIntegerField(verbose_name="Number's of Brothers"),
        ),
        migrations.AlterField(
            model_name='family',
            name='sister',
            field=models.PositiveIntegerField(verbose_name="Number's of Sisters"),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.FileField(help_text='Maximum file size allowed is 2Mb', unique=True, upload_to='male/passport', validators=[app.models.validate_image], verbose_name='Passport'),
        ),
    ]
