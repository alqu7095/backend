# Generated by Django 3.0.2 on 2020-01-07 22:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(default='ITEM', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('room_type', models.CharField(default='ROOM', max_length=50)),
                ('description', models.CharField(default='DEFAULT DESCRIPTION', max_length=500)),
                ('room_up', models.IntegerField(default=0)),
                ('room_down', models.IntegerField(default=0)),
                ('room_right', models.IntegerField(default=0)),
                ('room_left', models.IntegerField(default=0)),
                ('grid_x', models.IntegerField(default=None)),
                ('grid_y', models.IntegerField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('current_room', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
