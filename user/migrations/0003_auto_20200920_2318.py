# Generated by Django 3.1.1 on 2020-09-20 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200920_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=50, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='user',
            name='term',
            field=models.ManyToManyField(blank=True, null=True, related_name='term', to='user.Term'),
        ),
        migrations.AlterField(
            model_name='user',
            name='who',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='who', to='user.who'),
        ),
    ]
