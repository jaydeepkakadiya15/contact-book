# Generated by Django 5.1 on 2024-09-04 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_rename_contact_contactdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactdata',
            name='contact',
            field=models.IntegerField(max_length=100, unique=True),
        ),
    ]
