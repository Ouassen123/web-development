# Generated by Django 4.1.7 on 2023-04-01 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LocationVoitures', '0004_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.CharField(max_length=100)),
                ('Nom', models.CharField(max_length=20)),
                ('Message', models.CharField(max_length=1000)),
            ],
        ),
    ]
