# Generated by Django 3.1.3 on 2020-11-18 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20201118_0547'),
        ('user', '0003_auto_20201118_0600'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_tag_filter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.tag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'db_table': 'user_tag_filters',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='tag_filter',
            field=models.ManyToManyField(related_name='user_tags_filters', through='user.User_tag_filter', to='company.Tag'),
        ),
    ]