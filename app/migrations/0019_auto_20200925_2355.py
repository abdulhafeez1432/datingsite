# Generated by Django 3.1.1 on 2020-09-25 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_interestdata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='interestdata',
            old_name='intereser',
            new_name='interester',
        ),
        migrations.AlterField(
            model_name='interestdata',
            name='status',
            field=models.CharField(choices=[('A', 'INTREST'), ('L', 'LET US TALK'), ('S', 'LET US SEE'), {'FINAL STAGE', 'F'}], default='A', max_length=13),
        ),
    ]