import uuid
from django.db import models as m


"""
User model that contains the basic user columns
"""


class User(m.Model):
    id = m.CharField(default=uuid.uuid4, primary_key=True, max_length=36)
    first_name = m.CharField(max_length=128, blank=False)
    last_name = m.CharField(max_length=128, blank=False)
    city = m.CharField(max_length=128, blank=True)
    age = m.IntegerField(null=True, blank=True)

    class Meta(object):
        db_table = 'user'

