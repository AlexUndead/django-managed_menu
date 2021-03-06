# Generated by Django 3.0.1 on 2020-02-24 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('active', models.BooleanField(db_index=True, default=True, verbose_name='Активность')),
            ],
            options={
                'verbose_name': 'menu',
                'verbose_name_plural': 'menus',
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('order', models.IntegerField(default=500)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='managed_menu.Menu')),
            ],
            options={
                'verbose_name': 'menu item',
                'verbose_name_plural': 'menu items',
            },
        ),
    ]
