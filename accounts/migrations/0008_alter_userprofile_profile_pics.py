# Generated by Django 3.2.6 on 2021-10-16 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_userprofile_profile_pics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pics',
            field=models.ImageField(blank=True, default='img_avatar.png', upload_to='userprofile '),
        ),
    ]
