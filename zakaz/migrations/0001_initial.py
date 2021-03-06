# Generated by Django 3.0.4 on 2020-08-01 10:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lots', '0002_auto_20200801_1631'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zakazdoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daty', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата заявки')),
                ('status', models.CharField(choices=[('draft', ''), ('win', 'Выигрыш'), ('sended', 'Заявка отправлено')], default='draft', max_length=10)),
                ('klyenty', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='klyenty', to=settings.AUTH_USER_MODEL)),
                ('lots', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lots', to='lots.Article')),
            ],
            options={
                'verbose_name': 'Запрос документов',
                'verbose_name_plural': 'Запросы документов',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Zakaz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата заявки')),
                ('status', models.CharField(choices=[('draft', ''), ('win', 'В обработке'), ('send', 'Подача заявки'), ('sended', 'Обработан')], default='draft', max_length=10)),
                ('zavdate', models.DateTimeField(null=True, verbose_name='Дата завершения')),
                ('klyent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='klyent', to=settings.AUTH_USER_MODEL)),
                ('lot', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lot', to='lots.Article')),
            ],
            options={
                'verbose_name': 'Заявка на участие',
                'verbose_name_plural': 'Заявки на участие',
                'ordering': ['-id'],
            },
        ),
    ]
