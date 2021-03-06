# Generated by Django 2.1.5 on 2022-01-21 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20220120_1808'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empresa',
            options={'ordering': ['-created'], 'verbose_name': 'Empresa', 'verbose_name_plural': 'Empresas'},
        ),
        migrations.AlterModelOptions(
            name='tablaescalacion',
            options={'ordering': ['-created'], 'verbose_name': 'Tabla de Escalación', 'verbose_name_plural': 'Tablas de Escalaciones'},
        ),
        migrations.AddField(
            model_name='empresa',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='empresa', verbose_name='Adjunta una imagen'),
        ),
        migrations.AddField(
            model_name='tablaescalacion',
            name='order',
            field=models.IntegerField(blank=True, null=True, verbose_name='Teléfono'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_categoria', to='core.Categoria', verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='tablaescalacion',
            name='nivel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_nivel', to='core.Nivel', verbose_name='Nivel de Escalación o Cargo'),
        ),
        migrations.AlterField(
            model_name='tablaescalacion',
            name='phone',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Teléfono'),
        ),
    ]
