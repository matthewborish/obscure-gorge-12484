# Generated by Django 3.2.16 on 2023-03-02 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tool',
            name='category',
            field=models.CharField(default='general', max_length=100),
            preserve_default=False,
        ),
    ]
