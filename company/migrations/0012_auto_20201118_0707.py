# Generated by Django 3.1.3 on 2020-11-18 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0011_auto_20201118_0706'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='carrer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.carrer'),
        ),
        migrations.AddField(
            model_name='company',
            name='sub_tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_tags', to='company.sub_tag'),
        ),
    ]