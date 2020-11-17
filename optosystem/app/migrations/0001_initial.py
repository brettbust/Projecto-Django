# Generated by Django 3.1.3 on 2020-11-17 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pacientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20, verbose_name='nombre del paciente')),
                ('apellido', models.CharField(max_length=20, verbose_name='apellido del paciente')),
                ('edad', models.IntegerField(max_length=3, verbose_name='edad del paciente')),
                ('peso', models.FloatField(max_length=3, verbose_name='peso')),
                ('altura', models.FloatField(max_length=3, verbose_name='altura')),
            ],
        ),
        migrations.CreateModel(
            name='productos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_del_producto', models.CharField(max_length=20, verbose_name='nombre del producto')),
                ('precio_del_producto', models.FloatField(max_length=20, verbose_name='precio del producto')),
                ('subtotal', models.FloatField(max_length=20, verbose_name='subtotal')),
            ],
        ),
        migrations.CreateModel(
            name='turnos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_de_turno', models.DateField(verbose_name='fecha de turno')),
                ('medico_asignado', models.CharField(max_length=20, verbose_name='medico asignado')),
                ('relacion_con_pacientes', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.pacientes')),
            ],
        ),
        migrations.CreateModel(
            name='pedidos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_del_pedido', models.CharField(max_length=20, verbose_name='estado del pedido')),
                ('tipo_de_pago', models.CharField(max_length=20, verbose_name='tipo de pago')),
                ('relacion_con_productos', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.productos')),
            ],
        ),
        migrations.AddField(
            model_name='pacientes',
            name='relacion_con_pedidos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.pedidos'),
        ),
        migrations.CreateModel(
            name='historial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('historial_medico', models.CharField(max_length=200, verbose_name='historial medico')),
                ('relacion_con_pacientes', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.pacientes')),
            ],
        ),
    ]
