# Generated by Django 3.1.3 on 2020-11-18 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20201118_0547'),
        ('user', '0002_achievement_award_grade_past_carrer_recommendation_resume'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'db_table': 'likes',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='likes',
            field=models.ManyToManyField(related_name='likes', through='user.Like', to='company.Company'),
        ),
    ]
