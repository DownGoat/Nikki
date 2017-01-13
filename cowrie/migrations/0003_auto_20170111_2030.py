# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-11 19:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cowrie', '0002_sshsession_version'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sshsession',
            old_name='session_id',
            new_name='session',
        ),
        migrations.RenameField(
            model_name='sshsession',
            old_name='source_ip',
            new_name='src_ip',
        ),
        migrations.RenameField(
            model_name='sshsession',
            old_name='source_port',
            new_name='src_port',
        ),
        migrations.RemoveField(
            model_name='sshsession',
            name='destination_ip',
        ),
        migrations.RemoveField(
            model_name='sshsession',
            name='destination_port',
        ),
    ]