# Generated by Django 4.0 on 2022-01-31 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0002_alter_clause_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clause',
            name='ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.sentence'),
        ),
    ]