# Generated by Django 4.1.7 on 2023-04-01 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LocationVoitures', '0005_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='Lu',
            field=models.BooleanField(default=False),
        ),
    ]
