# Generated by Django 3.1.1 on 2020-09-22 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20200921_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='term',
            field=models.ManyToManyField(blank=True, null=True, related_name='_user_term_+', to='user.Term'),
        ),
    ]
