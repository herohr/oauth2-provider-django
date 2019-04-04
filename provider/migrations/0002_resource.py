# Generated by Django 2.0.2 on 2019-04-03 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('resource_id', models.AutoField(primary_key=True, serialize=False)),
                ('context', models.TextField(verbose_name='Jesus of Context')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='provider.User')),
            ],
        ),
    ]
