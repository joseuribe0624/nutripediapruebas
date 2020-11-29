# Generated by Django 3.0.5 on 2020-05-29 00:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0006_auto_20200527_0014"),
    ]

    operations = [
        migrations.AddField(
            model_name="paciente",
            name="nutricionista",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
