# Generated by Django 3.1.3 on 2020-11-18 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carrer', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'carrers',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('title', models.CharField(max_length=45)),
                ('dead_line', models.CharField(max_length=45)),
                ('image_url', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'companies',
            },
        ),
        migrations.CreateModel(
            name='District_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'district_categories',
            },
        ),
        migrations.CreateModel(
            name='Maincategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'maincategories',
            },
        ),
        migrations.CreateModel(
            name='Sub_tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'sub_tag',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'tags',
            },
        ),
        migrations.CreateModel(
            name='Tag_company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.company')),
                ('sub_tags', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.sub_tag')),
            ],
            options={
                'db_table': 'tag_companies',
            },
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('maincategories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.maincategory')),
            ],
            options={
                'db_table': 'subcategories',
            },
        ),
        migrations.AddField(
            model_name='sub_tag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.tag'),
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carrer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.carrer')),
                ('maincategories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.maincategory')),
                ('subcategories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.subcategory')),
            ],
            options={
                'db_table': 'salaries',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('district_categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.district_category')),
            ],
            options={
                'db_table': 'districts',
            },
        ),
    ]
