# Generated by Django 2.2.6 on 2020-03-03 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_auto_20200303_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='committeefeedback',
            name='berkeley_perception',
            field=models.IntegerField(blank=True, choices=[(0, 'Blank'), (1, 'No'), (2, 'No change/unsure'), (3, 'Yes')], default=0),
        ),
    ]
