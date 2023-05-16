# Generated by Django 4.2.1 on 2023-05-15 21:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productentry',
            old_name='product_list',
            new_name='product_list_id',
        ),
        migrations.RemoveField(
            model_name='productentry',
            name='product',
        ),
        migrations.AddField(
            model_name='productentry',
            name='product_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
        migrations.AlterField(
            model_name='productentry',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
    ]