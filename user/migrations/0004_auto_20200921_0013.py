# Generated by Django 3.1.1 on 2020-09-20 23:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20200920_2318'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='who',
            options={'verbose_name': 'Who', 'verbose_name_plural': 'Who'},
        ),
        migrations.RenameField(
            model_name='user',
            old_name='is_student',
            new_name='is_female',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='is_teacher',
            new_name='is_male',
        ),
    ]