# Generated by Django 4.2.3 on 2023-07-11 19:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0007_alter_user_date_joined"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="date_joined",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 7, 11, 19, 7, 20, 556496, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
