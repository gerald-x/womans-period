# Generated by Django 3.1.3 on 2021-10-13 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PeriodData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_period', models.DateField()),
                ('cycle_average', models.IntegerField()),
                ('period_average', models.IntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ProcessedData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period_start_date', models.DateField()),
                ('period_end_data', models.DateField()),
                ('ovulation_date', models.DateField()),
                ('fertility_window', models.DateField()),
                ('pre_ovulation_window', models.CharField(max_length=20)),
                ('post_ovulation_window', models.CharField(max_length=20)),
                ('raw_data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='periodapi.perioddata')),
            ],
        ),
    ]
