# Generated by Django 4.2.6 on 2023-10-08 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_contact_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='location',
            field=models.CharField(default='arizona', max_length=1000),
            preserve_default=False,
        ),
    ]
