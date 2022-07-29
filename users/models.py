import uuid
from django.db import models as m
from django.utils.translation import gettext_lazy as _


class GenderType(m.TextChoices):
    MALE = 'MALE', _('MALE')
    FEMALE = 'FEMALE', _('FEMALE')


class User(m.Model):
    id = m.CharField(default=uuid.uuid4, primary_key=True, max_length=36)
    name = m.CharField(max_length=128, blank=False)
    email = m.CharField(max_length=200, blank=True, unique=True)
    gender = m.CharField(
        max_length=128, null=True, choices=GenderType.choices
    )
    age = m.IntegerField(null=True, blank=True)

    class Meta(object):
        db_table = 'user'

