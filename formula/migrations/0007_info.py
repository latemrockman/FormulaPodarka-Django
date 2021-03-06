# Generated by Django 4.0.4 on 2022-06-15 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formula', '0006_product_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(default='', max_length=20)),
                ('logo', models.CharField(default='', max_length=40)),
                ('head_date', models.CharField(default='', max_length=10)),
                ('head_date_title', models.CharField(default='', max_length=50)),
                ('head_date_слоган', models.CharField(default='', max_length=50)),
                ('company_name', models.CharField(default='', max_length=50)),
                ('company_adress', models.CharField(default='', max_length=50)),
                ('work_schedule', models.CharField(default='', max_length=50)),
                ('legal_name', models.CharField(default='', max_length=50)),
                ('inn', models.CharField(default='', max_length=50)),
                ('ogrn', models.CharField(default='', max_length=50)),
                ('legal_adress', models.CharField(default='', max_length=50)),
                ('general_manager', models.CharField(default='', max_length=50)),
                ('karta', models.CharField(default='', max_length=200)),
                ('meta_tags', models.TextField()),
            ],
        ),
    ]
