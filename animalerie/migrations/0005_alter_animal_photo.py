# Generated by Django 3.2.9 on 2021-11-25 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animalerie', '0004_alter_equipement_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='photo',
            field=models.ImageField(upload_to='media/id_animal'),
        ),
    ]
