# Generated by Django 3.2.25 on 2024-04-28 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('template_marketplace', '0003_document_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='file',
            field=models.FileField(upload_to='documents/'),
        ),
    ]