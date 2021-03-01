# Generated by Django 2.2 on 2021-03-01 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DB_apis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.CharField(max_length=10, null=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('api_method', models.CharField(max_length=10, null=True)),
                ('api_url', models.CharField(max_length=1000, null=True)),
                ('api_header', models.CharField(max_length=1000, null=True)),
                ('api_login', models.CharField(max_length=10, null=True)),
                ('api_host', models.CharField(max_length=100, null=True)),
                ('des', models.CharField(max_length=100, null=True)),
                ('body_method', models.CharField(max_length=20, null=True)),
                ('api_body', models.CharField(max_length=1000, null=True)),
                ('result', models.TextField(null=True)),
                ('sign', models.CharField(max_length=10, null=True)),
                ('file_key', models.CharField(max_length=50, null=True)),
                ('file_name', models.CharField(max_length=50, null=True)),
                ('public_header', models.CharField(max_length=1000, null=True)),
                ('last_body_method', models.CharField(max_length=20, null=True)),
                ('last_api_body', models.CharField(max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DB_diss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=30, null=True)),
                ('text', models.CharField(max_length=1000, null=True)),
                ('ctime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='DB_home_href',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('href', models.CharField(max_length=2000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DB_project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('remark', models.CharField(max_length=1000, null=True)),
                ('user', models.CharField(max_length=15, null=True)),
                ('other_user', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
