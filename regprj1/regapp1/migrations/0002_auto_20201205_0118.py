# Generated by Django 3.1.3 on 2020-12-05 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regapp1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='regapp1/media/profile_pics'),
        ),
    ]
