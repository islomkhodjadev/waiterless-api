# Generated by Django 5.1 on 2024-08-21 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(default=1, upload_to='user/images'),
            preserve_default=False,
        ),
    ]
