# Generated by Django 3.1.1 on 2020-09-22 19:04

import app.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateField(verbose_name='Date of Birth')),
                ('tribe', models.CharField(choices=[('Yourba', 'Yoruba'), ('Hausa', 'Hausa')], max_length=500, verbose_name='Tribe')),
                ('language', models.CharField(choices=[('Yourba', 'Yoruba'), ('Hausa', 'Hausa')], max_length=150, verbose_name='Language Spoken')),
                ('place_of_birth', models.CharField(max_length=150, verbose_name='Place of Birth')),
                ('body_complex', models.CharField(choices=[('Light', 'Light'), ('Dark', 'Dark')], max_length=50, verbose_name='Complex')),
                ('marital', models.CharField(choices=[('Divorced', 'Divorced'), ('Married', 'Married'), ('Never Married', 'Never Married'), ('Widowed', 'Widowed')], max_length=150, verbose_name='Martial Status')),
                ('height', models.CharField(choices=[('4cm - 5cm', '4cm - 5cm'), ('5cm - 6cm', '6cm - 7cm')], max_length=50, verbose_name='Height')),
                ('body', models.CharField(choices=[('Athlete', 'Athlete'), ('Average', 'Average'), ('Heavy', 'Heavy'), ('Slim', 'Slim')], max_length=50, verbose_name='Body Type')),
                ('physical', models.CharField(choices=[('Challenged', 'Challenged'), ('Normal', 'Normal')], max_length=150, verbose_name='Physical Challenges')),
                ('image', models.FileField(help_text='Maximum file size allowed is 2Mb', unique=True, upload_to='male/passport', validators=[app.models.validate_image])),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('father_name', models.CharField(max_length=50, verbose_name="Father's Name")),
                ('father_job', models.CharField(max_length=50, verbose_name="Ftaher's Job")),
                ('mother', models.CharField(max_length=50, verbose_name="Mother's Name")),
                ('mother_job', models.CharField(max_length=50, verbose_name="Mother's Job")),
                ('sister', models.CharField(max_length=50, verbose_name="Number's of Sisters")),
                ('brother', models.CharField(max_length=50, verbose_name="Number's of Brothers")),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='family', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Family',
                'verbose_name_plural': 'Familys',
            },
        ),
        migrations.CreateModel(
            name='Eductaion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.CharField(choices=[('Web Development', 'Web Development'), ('Software Development', 'Software Development')], max_length=250, verbose_name='Job Type')),
                ('job_description', models.CharField(max_length=500, verbose_name='Job Description')),
                ('education', models.CharField(choices=[('PhD', 'PhD'), ('BSc.', 'BSc')], max_length=250, verbose_name='Education')),
                ('education_description', models.CharField(max_length=500, verbose_name='education Description')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='education', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Eductaion',
                'verbose_name_plural': 'Eductaions',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('status', models.CharField(choices=[('Citizen', 'Citizen'), ('Student', 'Student')], max_length=150, verbose_name='Citizen Status')),
                ('state', models.CharField(max_length=50, verbose_name='State')),
                ('city', models.CharField(max_length=50, verbose_name='City')),
                ('address', models.CharField(max_length=250, verbose_name='Personal Address')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='contact', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_me', models.TextField(verbose_name='About My Partner')),
                ('beards', models.BooleanField(default=True, verbose_name='Do You Keep Beards')),
                ('religious', models.CharField(choices=[('Muslim Since Birth', 'Muslim Since Birth'), ('Revert Muslim', 'Revert Muslim')], max_length=250, verbose_name='Religion History')),
                ('availablity', models.CharField(choices=[('Currently available for Nikkah', 'Currently available for Nikkah'), ('Currently not available for Nikkah', 'Currently not available for Nikkah')], max_length=500, verbose_name='Availability Status')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='aboutme', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'AboutMe',
                'verbose_name_plural': 'AboutMes',
            },
        ),
    ]