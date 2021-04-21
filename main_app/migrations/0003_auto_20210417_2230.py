# Generated by Django 3.2 on 2021-04-17 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_knob'),
    ]

    operations = [
        migrations.AddField(
            model_name='knob',
            name='pedal',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='main_app.pedal'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='knob',
            name='current_value',
            field=models.FloatField(verbose_name='Current Value'),
        ),
        migrations.AlterField(
            model_name='knob',
            name='max_value',
            field=models.IntegerField(verbose_name='Max Value'),
        ),
        migrations.AlterField(
            model_name='knob',
            name='setting_name',
            field=models.CharField(max_length=16, verbose_name='Setting Name'),
        ),
    ]