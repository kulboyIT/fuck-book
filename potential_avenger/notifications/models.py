import random
from datetime import date

from django.db import models

from users.models import Person
from hardcoded_models.models import TipsList


class PeriodicalNotification (models.Model):
    person = models.ForeignKey(Person)
    message = models.CharField(
        'Notification Message',
        max_length=255,
        default="Haven't checked-in in a while. Sex life getting slow?")
    date_saved = models.DateField(default=date.today())
    unread = models.BooleanField(default=True)


def create_tip_message():
    try:
        tip_message = random.choice(TipsList.objects.all())
    except IndexError:
        tip_message = "Sorry, no tips in the database."
    return tip_message


class TipNotification (models.Model):
    person = models.ForeignKey(Person)
    message = models.CharField('Notification Message', max_length=255, default=create_tip_message)
    date_saved = models.DateField(default=date.today())
    unread = models.BooleanField(default=True)


class DifferenceNotification (models.Model):
    person = models.ForeignKey(Person)
    message = models.CharField('Notification Message', max_length=255, default=" ")
    date_saved = models.DateField(default=date.today())
    unread = models.BooleanField(default=True)
