# Generated by Django 3.1.5 on 2021-01-21 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0002_auto_20210117_0026'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='last_report_message',
            field=models.TextField(default='', help_text='上一次填报返回信息'),
            preserve_default=False,
        ),
    ]