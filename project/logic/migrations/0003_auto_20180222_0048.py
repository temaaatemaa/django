# Generated by Django 2.0.2 on 2018-02-21 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0002_auto_20180220_2304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fulltable',
            name='priotiry',
        ),
        migrations.AddField(
            model_name='fulltable',
            name='priotiry',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='logic.Priority'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='fulltable',
            name='system',
        ),
        migrations.AddField(
            model_name='fulltable',
            name='system',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='logic.Systems'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='fulltable',
            name='time',
        ),
        migrations.AddField(
            model_name='fulltable',
            name='time',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='logic.Time'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='fulltable',
            name='user',
        ),
        migrations.AddField(
            model_name='fulltable',
            name='user',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='logic.Users'),
            preserve_default=False,
        ),
    ]
