# Generated by Django 3.1.3 on 2020-12-28 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_code', models.CharField(max_length=10)),
                ('game_creator', models.CharField(max_length=10)),
                ('game_oppenent', models.CharField(blank=True, max_length=10, null=True)),
                ('is_over', models.BooleanField(default=False)),
            ],
        ),
    ]
