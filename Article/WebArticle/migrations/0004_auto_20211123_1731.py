# Generated by Django 2.1.7 on 2021-11-23 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebArticle', '0003_auto_20211123_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='description',
            field=models.TextField(max_length=120),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='email',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='password',
            field=models.CharField(max_length=20),
        ),
    ]
