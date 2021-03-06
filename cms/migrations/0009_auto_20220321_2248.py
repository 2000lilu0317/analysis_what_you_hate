# Generated by Django 2.1.15 on 2022-03-21 13:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0008_userpostmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpostmodel',
            name='username',
        ),
        migrations.AddField(
            model_name='userpostmodel',
            name='create_user',
            field=models.ForeignKey(default=999, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userpostmodel',
            name='no_one',
            field=models.CharField(blank=True, max_length=280, verbose_name='no_one'),
        ),
        migrations.AlterField(
            model_name='userpostmodel',
            name='no_two',
            field=models.CharField(blank=True, max_length=280, verbose_name='no_one'),
        ),
    ]
