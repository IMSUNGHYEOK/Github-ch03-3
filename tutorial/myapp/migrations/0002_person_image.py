# Generated by Django 2.0.5 on 2018-05-24 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='image',
            field=models.ImageField(default='default_image.jpeg', upload_to=''),
        ),
    ]
