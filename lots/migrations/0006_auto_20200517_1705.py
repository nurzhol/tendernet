# Generated by Django 3.0.4 on 2020-05-17 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lots', '0005_auto_20200517_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='city',
            field=models.ForeignKey(default=2, null=True, on_delete=django.db.models.deletion.PROTECT, to='lots.Cities', verbose_name='Город'),
        ),
    ]
