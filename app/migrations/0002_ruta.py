# Generated by Django 3.2.9 on 2021-12-14 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ruta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origen', models.CharField(max_length=50)),
                ('destino', models.CharField(max_length=50)),
                ('kilometros', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('camion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rutas', to='app.camion')),
            ],
        ),
    ]