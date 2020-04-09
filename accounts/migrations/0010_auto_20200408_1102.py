# Generated by Django 3.0.5 on 2020-04-08 05:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0009_auto_20200404_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grades',
            name='branch',
            field=models.CharField(default='Chemical Engineering', max_length=200),
        ),
        migrations.AlterField(
            model_name='grades',
            name='lastsemester',
            field=models.FloatField(default=9.69),
        ),
        migrations.AlterField(
            model_name='grades',
            name='total',
            field=models.FloatField(default=9.717),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]