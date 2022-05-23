# Generated by Django 4.0.4 on 2022-05-23 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.AddField(
            model_name='product',
            name='completed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]