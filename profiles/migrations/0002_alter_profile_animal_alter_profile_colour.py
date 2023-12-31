# Generated by Django 4.2.3 on 2023-07-20 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="animal",
            field=models.CharField(
                default="If you were an animal what animal would you like to be?",
                max_length=150,
                verbose_name="Animal",
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="colour",
            field=models.CharField(
                default="What is your favourite color?",
                max_length=150,
                verbose_name="Colour",
            ),
        ),
    ]
