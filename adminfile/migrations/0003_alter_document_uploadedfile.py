# Generated by Django 4.0.3 on 2022-03-31 13:30

import adminfile.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminfile', '0002_alter_document_uploadedfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='uploadedFile',
            field=models.FileField(storage=adminfile.models.OverwriteStorage, upload_to='result/'),
        ),
    ]
