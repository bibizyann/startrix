# Generated by Django 5.0.2 on 2024-04-13 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0005_alter_allsourceusersenriched_contacts_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allsourceusersenriched',
            name='id',
        ),
        migrations.AlterField(
            model_name='allsourceusersenriched',
            name='user_id',
            field=models.CharField(primary_key=True, serialize=False),
        ),
    ]
