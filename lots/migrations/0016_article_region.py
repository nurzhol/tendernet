# Generated by Django 3.0.4 on 2020-05-25 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lots', '0015_auto_20200525_1951'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='lots.Regions', verbose_name='Область'),
        ),
    ]