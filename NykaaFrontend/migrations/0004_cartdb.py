# Generated by Django 4.2.7 on 2024-01-09 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NykaaFrontend', '0003_registerdb_confirmpassword'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(blank=True, max_length=100, null=True)),
                ('Pro_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Quantity', models.IntegerField(blank=True, null=True)),
                ('Price', models.IntegerField(blank=True, null=True)),
                ('Total_Price', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
