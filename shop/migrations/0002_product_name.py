# Generated by Django 3.0 on 2019-12-08 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default='default product', max_length=256),
            preserve_default=False,
        ),
    ]