# Generated by Django 4.1.2 on 2022-10-16 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media_management', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='media',
            name='full_path',
        ),
        migrations.AddField(
            model_name='media',
            name='media_file',
            field=models.FileField(max_length=300, null=True, upload_to='user_uploads/%Y/%m/%d/'),
        ),
    ]
