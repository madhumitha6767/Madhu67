# Generated by Django 3.0 on 2021-04-02 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UsrRg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=120)),
                ('password', models.CharField(max_length=120)),
                ('email', models.CharField(max_length=120)),
                ('age', models.IntegerField(default=10)),
            ],
        ),
    ]
