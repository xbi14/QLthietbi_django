# Generated by Django 4.1.7 on 2023-05-19 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QLthietbi_app', '0002_alter_thietbi_hinh_anh'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thietbi',
            name='id_thiet_bi',
            field=models.CharField(editable=False, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
    ]
