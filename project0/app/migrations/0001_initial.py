# Generated by Django 4.0 on 2023-07-21 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacher_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('address', models.DateTimeField(blank=True, null=True)),
                ('updated_by', models.CharField(max_length=50, null=True)),
                ('updated_on', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]