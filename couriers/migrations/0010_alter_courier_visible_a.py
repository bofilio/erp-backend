# Generated by Django 3.2.10 on 2022-04-27 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('couriers', '0009_expediteur_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courier',
            name='visible_a',
            field=models.ManyToManyField(null=True, related_name='couriers_visibles', to='couriers.Expediteur', verbose_name='Visible à'),
        ),
    ]
