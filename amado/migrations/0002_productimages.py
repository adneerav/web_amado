# Generated by Django 2.2.12 on 2020-04-10 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('amado', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_prod', models.ImageField(upload_to='prod_images')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amado.Products')),
            ],
        ),
    ]
