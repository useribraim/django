# Generated by Django 4.0.6 on 2022-08-11 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sentence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_position', models.CharField(max_length=50)),
                ('text', models.CharField(max_length=3000)),
                ('document_ID', models.CharField(max_length=50)),
                ('ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_api.document')),
            ],
        ),
    ]
