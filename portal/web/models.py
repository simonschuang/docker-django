# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class General(models.Model):
    _id = models.IntField(default=0)
    name = models.CharField(max_length=30)
    machine_uuid = models.CharField(max_length=60)
    serial_number = models.CharField(max_length=60)
