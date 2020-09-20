# Generated by Django 3.1.1 on 2020-09-20 14:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('gaming', '0018_auto_20200916_1116'),
        ('authentication', '0005_auto_20200916_1015'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='gaming.game')),
                ('user_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
