# Generated by Django 2.1.7 on 2019-08-17 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='email',
            new_name='emailAddress',
        ),
        migrations.AddField(
            model_name='order',
            name='billingAddress1',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='order',
            name='billingCity',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
