# Generated by Django 5.0.6 on 2024-06-26 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Academido', '0002_boton'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
            ],
        ),
    ]
