# Generated by Django 4.2 on 2023-05-01 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodDeliveryTechnovizor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
