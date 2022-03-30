# Generated by Django 3.2.10 on 2022-03-22 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('couriers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='courier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='couriers.courier'),
        ),
        migrations.AlterField(
            model_name='courier',
            name='n_enregistrement',
            field=models.CharField(max_length=255, verbose_name='N° Enrigestrement Local'),
        ),
        migrations.AlterField(
            model_name='courier',
            name='referance_exp',
            field=models.CharField(max_length=255, verbose_name='Réferance Expéditeur'),
        ),
        migrations.AlterField(
            model_name='courier',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='couriers.status', verbose_name='Traitement'),
        ),
        migrations.AlterField(
            model_name='courier',
            name='visible_a',
            field=models.ManyToManyField(related_name='couriers_visibles', to='couriers.Entity', verbose_name='Visible à'),
        ),
    ]
