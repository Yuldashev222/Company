# Generated by Django 4.0.3 on 2022-03-10 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_company_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='name',
            new_name='company_name',
        ),
    ]
