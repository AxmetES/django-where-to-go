# Generated by Django 3.0.7 on 2020-07-12 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_remove_image_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='position',
            field=models.PositiveIntegerField(default=True),
        ),
    ]