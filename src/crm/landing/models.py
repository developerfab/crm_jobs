# -*- coding: utf-8 -*-
from django.db import models

TYPE_CONTACT_USER_CHOICES = (
    (1, 'Developer'),
    (2, 'Compañia'),
)


class ContactUser(models.Model):
    name = models.CharField(max_length=200)
    kind = models.IntegerField(choices=TYPE_CONTACT_USER_CHOICES)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True, null=True)
