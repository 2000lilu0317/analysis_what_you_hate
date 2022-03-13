# Generated by Django 2.1.15 on 2022-03-13 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_user_twitter'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_one', models.CharField(blank=True, max_length=150)),
                ('no_two', models.CharField(blank=True, max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='no_one',
            field=models.CharField(blank=True, max_length=150, verbose_name='no_one'),
        ),
        migrations.AddField(
            model_name='user',
            name='no_two',
            field=models.CharField(blank=True, max_length=150, verbose_name='no_two'),
        ),
    ]
