# Generated by Django 2.1.5 on 2019-02-23 01:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0004_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='item_list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecom.Item'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ecom.Person'),
        ),
    ]
