# Generated by Django 5.1.7 on 2025-04-04 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0009_alter_contactdata_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactdata',
            name='emaill',
        ),
        migrations.AddField(
            model_name='contactdata',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='contactdata',
            name='address',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='contactdata',
            name='city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='contactdata',
            name='contact',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='contactdata',
            name='gender',
            field=models.CharField(max_length=10),
        ),
    ]
