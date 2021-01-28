# Generated by Django 3.1.5 on 2021-01-29 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MAIN', '0002_auto_20210128_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='loans',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='MAIN.account'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offers',
            name='investor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='MAIN.account'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offers',
            name='loan',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='MAIN.loans'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
    ]