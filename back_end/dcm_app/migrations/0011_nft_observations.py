# Generated by Django 4.0.1 on 2022-01-30 01:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dcm_app', '0010_remove_nft_observations'),
    ]

    operations = [
        migrations.AddField(
            model_name='nft',
            name='observations',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='observation', to='dcm_app.observation'),
        ),
    ]
