# Generated by Django 3.0.4 on 2020-08-01 10:31

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=None, max_length=30, verbose_name='Код')),
                ('name', models.CharField(db_index=True, max_length=30, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Regions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=None, max_length=30, verbose_name='Код')),
                ('name', models.CharField(db_index=True, max_length=30, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Область',
                'verbose_name_plural': 'районы',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=99, null=True, verbose_name='Единица измерения')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='FavoriteSearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_query', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='search_query', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xml_id', models.CharField(max_length=255, null=True, unique=True, verbose_name='Внешний код для Api')),
                ('customer_bin', models.CharField(max_length=255, null=True, verbose_name='Бин организатора')),
                ('title', models.CharField(max_length=255, null=True, verbose_name='Наименование лота')),
                ('lotFullName', models.CharField(max_length=255, null=True, verbose_name='Полное имя лота')),
                ('itemZakup', models.CharField(choices=[('product', 'Товар'), ('services', 'Услуги'), ('job', 'Работа')], default='product', max_length=255, verbose_name='Предмет закупки')),
                ('customer', models.CharField(max_length=255, null=True, verbose_name='Заказчик')),
                ('addressFull', models.CharField(max_length=255, null=True, verbose_name='Место постаки, полный адресс')),
                ('numb', models.CharField(max_length=150, null=True, verbose_name='Номер лота')),
                ('price', models.FloatField(null=True, verbose_name='Цена')),
                ('count', models.IntegerField(null=True, verbose_name='Количество')),
                ('statzakup', models.CharField(choices=[('draft', 'Запрос ценовых предложении'), ('win', 'Конкурс'), ('sended', 'Аукцион')], default='draft', max_length=10, verbose_name='Способ закупки')),
                ('date_open', models.DateTimeField(null=True, verbose_name='Дата открытия')),
                ('date', models.DateTimeField(null=True, verbose_name='Дата закрытия')),
                ('date_created', models.DateTimeField(default=datetime.datetime(2020, 8, 1, 10, 31, 13, 197410, tzinfo=utc), verbose_name='Дата создания')),
                ('yst', models.URLField(max_length=255, null=True, verbose_name='Ссылка')),
                ('status', models.BooleanField(db_index=True, default=True, null=True, verbose_name='Опубликован')),
                ('slug', models.SlugField(max_length=255)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='lots.Cities', verbose_name='Город')),
                ('favourite', models.ManyToManyField(blank=True, related_name='favourite', to=settings.AUTH_USER_MODEL)),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='lots.Regions', verbose_name='Область')),
                ('unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='lots.Unit', verbose_name='Единица измерения')),
            ],
            options={
                'verbose_name': 'Лот',
                'verbose_name_plural': 'Лоты',
            },
        ),
    ]
