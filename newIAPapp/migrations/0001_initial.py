# Generated by Django 4.1.4 on 2022-12-08 20:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Задача')),
                ('descr', models.CharField(max_length=50, verbose_name='Описание')),
                ('freq', models.CharField(choices=[('ON', 'единоразовая'), ('DA', 'ежедневная'), ('WE', 'еженедельная'), ('MO', 'ежемесячная')], default='ON', max_length=20, verbose_name='Повторяемость')),
                ('sphere', models.CharField(choices=[('ST', 'учеба'), ('WO', 'работа'), ('HE', 'здоровье'), ('HO', 'хобби'), ('OT', 'иное')], default='OT', max_length=20, verbose_name='Сфера')),
                ('imp', models.CharField(choices=[('WE', 'желательно'), ('IM', 'важно'), ('CR', 'критически важно'), ('LI', 'жизненно важно')], default='WE', max_length=20, verbose_name='Важность')),
                ('deadline', models.DateTimeField(verbose_name='Крайний срок')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
