# Generated by Django 4.0.1 on 2022-01-26 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('affairs', '0002_myuser_email_myuser_repeatpassword_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intake',
            name='edate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='intake',
            name='sdate',
            field=models.DateField(),
        ),
    ]