# Generated by Django 3.0.5 on 2020-05-23 22:37

from django.db import migrations, models
import shortuuidfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Alimentacion",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nombre_alimento",
                    models.CharField(blank=True, max_length=30, verbose_name="nombres"),
                ),
                ("descripcion", models.TextField(default="")),
                ("unidad", models.FloatField(blank=True, default=None, null=True)),
                ("cant_sodio", models.FloatField(blank=True, default=None, null=True)),
                ("cant_calcio", models.FloatField(blank=True, default=None, null=True)),
                (
                    "cant_magnesio",
                    models.FloatField(blank=True, default=None, null=True),
                ),
                ("calorias", models.FloatField(blank=True, default=None, null=True)),
                ("proteina", models.FloatField(blank=True, default=None, null=True)),
                (
                    "carbohidratos",
                    models.FloatField(blank=True, default=None, null=True),
                ),
                ("grasas", models.FloatField(blank=True, default=None, null=True)),
                ("lista_negra", models.BooleanField(default=False)),
                (
                    "uuid",
                    shortuuidfield.fields.ShortUUIDField(
                        blank=True, editable=False, max_length=22
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
    ]
