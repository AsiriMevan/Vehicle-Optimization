# Generated by Django 4.0 on 2022-01-21 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('myapp', '0003_alter_client_history_history_deliveries'),
    ]

    operations = [
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('warehouse_name', models.CharField(max_length=255)),
                ('warehouse_description', models.TextField()),
                ('warehouse_location', models.CharField(max_length=255)),
                ('geofence_details', models.CharField(max_length=10000)),
                ('status', models.CharField(choices=[('FUNCTIONAL', 'FUNCTIONAL'), ('CLOSED', 'CLOSED')], default='FUNCTIONAL', max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='client',
            name='client_description',
            field=models.TextField(),
        ),
        migrations.CreateModel(
            name='Warehouse_vehicles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigned_vehicles', models.CharField(max_length=255)),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='warehouse_vehicles', to='myapp.warehouse')),
            ],
            options={
                'verbose_name_plural': 'warehouse_vehicles',
                'ordering': ('-assigned_vehicles',),
            },
        ),
        migrations.CreateModel(
            name='Warehouse_history',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='warehouse_creator1', to='auth.user')),
                ('history_deliveries', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history1', to='myapp.client_deliveries')),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='warehouse_history', to='myapp.warehouse')),
            ],
            options={
                'verbose_name_plural': 'warehouse_history',
                'ordering': ('-history_deliveries',),
            },
        ),
        migrations.CreateModel(
            name='Warehouse_deliveries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scheduled_deliveries', models.DateTimeField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='warehouse_creator', to='auth.user')),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='warehouse_deliveries', to='myapp.warehouse')),
            ],
            options={
                'verbose_name_plural': 'warehouse_deliveries',
                'ordering': ('-scheduled_deliveries',),
            },
        ),
    ]