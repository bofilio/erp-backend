# Generated by Django 3.2.10 on 2022-04-24 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('couriers', '0008_auto_20220423_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='expediteur',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]