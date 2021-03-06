# Generated by Django 3.1.1 on 2020-09-16 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gaming', '0007_auto_20200915_1646'),
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='description',
            field=models.TextField(default=None),
        ),
        migrations.RemoveField(
            model_name='game',
            name='developers',
        ),
        migrations.AddField(
            model_name='game',
            name='developers',
            field=models.ManyToManyField(default=None, related_name='developers', to='gaming.Developer'),
        ),
    ]
