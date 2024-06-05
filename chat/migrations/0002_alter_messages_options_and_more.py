# Generated by Django 5.0.3 on 2024-04-02 12:10

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='messages',
            options={'ordering': ('timestamp',)},
        ),
        migrations.RenameField(
            model_name='messages',
            old_name='description',
            new_name='message',
        ),
        migrations.AddField(
            model_name='messages',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
