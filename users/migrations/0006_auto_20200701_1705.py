# Generated by Django 3.0.4 on 2020-07-01 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200701_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='tarif',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Price', verbose_name='Тариф'),
        ),
    ]
