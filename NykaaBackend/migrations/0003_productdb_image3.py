# Generated by Django 4.2.7 on 2024-01-03 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NykaaBackend', '0002_rename_image_productdb_image1_productdb_image2'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdb',
            name='Image3',
            field=models.ImageField(blank=True, null=True, upload_to='Product Images'),
        ),
    ]
