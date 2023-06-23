# Generated by Django 4.2.2 on 2023-06-22 17:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('financial_goal', models.IntegerField(default=3)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=350)),
                ('rate', models.IntegerField()),
                ('assigned_to', models.ManyToManyField(related_name='assigning', to='pickpayapi.child')),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monthly_budget', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JobAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=False)),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pickpayapi.child')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pickpayapi.job')),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pickpayapi.parent'),
        ),
    ]
