# Generated by Django 3.0.8 on 2020-07-14 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_offers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Offers',
            new_name='Offer',
        ),
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]
