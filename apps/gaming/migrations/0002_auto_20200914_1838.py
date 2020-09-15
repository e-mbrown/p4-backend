# Generated by Django 3.1.1 on 2020-09-14 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gaming', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='banner',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='game',
            name='cover',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='game',
            name='developers',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AddField(
            model_name='game',
            name='name',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='game',
            name='platforms',
            field=models.ManyToManyField(default=None, to='gaming.Platform'),
        ),
        migrations.AddField(
            model_name='game',
            name='rating',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AddField(
            model_name='game',
            name='region',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='game',
            name='release_date',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='review',
            name='game',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='gaming.game'),
        ),
        migrations.AddField(
            model_name='review',
            name='header',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='review',
            name='is_official',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='review',
            name='text',
            field=models.TextField(default=None),
        ),
    ]
