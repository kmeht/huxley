# Generated by Django 2.2.6 on 2020-03-03 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0038_auto_20200302_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='committeefeedback',
            name='berkeley_perception',
            field=models.IntegerField(blank=True, choices=[(1, 'No'), (0, 'No change/unsure'), (2, 'Yes')], default=0),
        ),
    ]
