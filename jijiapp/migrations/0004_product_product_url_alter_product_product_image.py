# Generated by Django 5.0.3 on 2024-06-17 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jijiapp', '0003_alter_product_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_url',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
