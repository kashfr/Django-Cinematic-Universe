# Generated by Django 4.0.1 on 2022-01-30 01:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dcm_app', '0008_remove_observation_nfts_nft_observations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nft',
            name='observations',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='observations', to='dcm_app.observation'),
        ),
    ]
