# Generated by Django 3.0.4 on 2020-05-03 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lots', '0002_article_purchase_method'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='body',
        ),
        migrations.RemoveField(
            model_name='article',
            name='purchase_method',
        ),
        migrations.AddField(
            model_name='article',
            name='customer',
            field=models.CharField(max_length=255, null=True, verbose_name='Заказчик'),
        ),
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(null=True, verbose_name='Дата закрытия'),
        ),
        migrations.AlterField(
            model_name='article',
            name='date_open',
            field=models.DateTimeField(null=True, verbose_name='Дата открытия'),
        ),
        migrations.AlterField(
            model_name='article',
            name='itemZakup',
            field=models.CharField(choices=[('product', 'Товар'), ('services', 'Услуги'), ('job', 'Работа')], default='product', max_length=255, verbose_name='Предмет закупки'),
        ),
        migrations.AlterField(
            model_name='article',
            name='totalLots',
            field=models.IntegerField(null=True, verbose_name='Кол-во лотов в объявлении'),
        ),
    ]