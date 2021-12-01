# Generated by Django 3.2.4 on 2021-07-07 02:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0004_auto_20210707_1044'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubModelForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=255, verbose_name='ユーザID')),
                ('quiz_id', models.IntegerField(default=0, verbose_name='クイズID')),
                ('text', models.CharField(max_length=8192, verbose_name='テキスト')),
                ('create_at', models.DateField(default=django.utils.timezone.now, verbose_name='提出日')),
            ],
        ),
    ]
