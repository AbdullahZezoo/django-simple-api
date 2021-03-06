# Generated by Django 3.1.5 on 2021-01-29 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MAIN', '0004_auto_20210129_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='loans',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='MAIN.account'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offers',
            name='investor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='investor', to='MAIN.account'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offers',
            name='loan',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='loan', to='MAIN.loans'),
            preserve_default=False,
        ),
    ]
