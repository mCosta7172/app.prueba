# Generated by Django 2.2.6 on 2019-12-06 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bases', '0012_auto_20191206_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agencia',
            name='codigo_postal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='codpostal', to='bases.Codigo_Postal'),
        ),
        migrations.CreateModel(
            name='CP_Agencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bases.Agencia')),
                ('codigo_postal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bases.Codigo_Postal')),
            ],
        ),
        migrations.AddField(
            model_name='agencia',
            name='localidades',
            field=models.ManyToManyField(through='bases.CP_Agencia', to='bases.Codigo_Postal'),
        ),
    ]
