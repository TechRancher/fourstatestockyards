# Generated by Django 2.1.7 on 2019-03-19 03:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SheepReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('market_Date', models.DateField(default=datetime.datetime.now)),
                ('sale_Type', models.CharField(default='Sheep/Goat', max_length=20)),
                ('type_Livestock', models.CharField(max_length=30)),
                ('head_Count', models.IntegerField(blank=True, null=True)),
                ('livestock_weight', models.CharField(choices=[('Weight', (('20-30', '20-30'), ('30-40', '30-40'), ('40-50', '40-50'), ('50-60', '50-60'), ('60-70', '60-70'), ('70-80', '70-80'), ('80-90', '80-90'), ('90-100', '90-100'), ('100-110', '100-110'), ('110-120', '110-120'), ('120-130', '120-130'), ('130-140', '130-140'), ('140-150', '140-150'), ('150-160', '150-160'), ('160-170', '160-170'), ('170-180', '170-180'), ('180-190', '180-190'), ('190-200', '190-200'), ('200-210', '200-210'), ('210-220', '210-220'), ('220-230', '220-230'))), ('Replacement Does', (('Replacement Does', 'Replacement Does'),)), ('Replacement Ewes', (('Replacement Ewes', 'Replacement Ewes'),))], default='20-30', max_length=20)),
                ('high_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('low_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('remarks', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]