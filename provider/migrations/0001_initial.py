# Generated by Django 2.0.2 on 2019-04-03 11:06

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllowedApp',
            fields=[
                ('app_id', models.AutoField(primary_key=True, serialize=False)),
                ('app_secret', models.CharField(max_length=256)),
                ('app_name', models.CharField(max_length=32)),
                ('access', models.TextField(choices=[('R', 'read'), ('W', 'write'), ('RW', 'read and write')])),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('client_id', models.AutoField(primary_key=True, serialize=False)),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='provider.AllowedApp')),
            ],
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('token_id', models.UUIDField(auto_created=True, default=uuid.uuid4, primary_key=True, serialize=False)),
                ('access_token', models.CharField(max_length=256)),
                ('refresh_token', models.CharField(max_length=256, null=True)),
                ('access_token_expiration', models.BigIntegerField()),
                ('refresh_token_expiration', models.BigIntegerField()),
                ('scope', models.CharField(max_length=32, verbose_name='Access range')),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='provider.AllowedApp')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='provider.Client')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='token',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='provider.User'),
        ),
    ]