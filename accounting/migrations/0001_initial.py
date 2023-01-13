# Generated by Django 3.2 on 2023-01-12 11:42

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
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Должность')),
                ('department', models.CharField(max_length=50, verbose_name='Отдел')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=50, verbose_name='ФИО')),
                ('birth_date', models.DateField(verbose_name='Дата рождения')),
                ('salary', models.FloatField(verbose_name='Зарплата')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.position')),
            ],
        ),
    ]