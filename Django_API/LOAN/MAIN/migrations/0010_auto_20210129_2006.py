# Generated by Django 3.1.5 on 2021-01-29 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MAIN', '0009_auto_20210129_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loans',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='MAIN.account'),
        ),
        migrations.AlterField(
            model_name='offers',
            name='investor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='investor', to='MAIN.account'),
        ),
        migrations.AlterField(
            model_name='offers',
            name='loan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loan', to='MAIN.loans'),
        ),
    ]
