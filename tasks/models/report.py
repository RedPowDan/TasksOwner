import inspect
import os

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from tasks.base_models import BaseModel


class Report(BaseModel):
    date = models.DateField(
        verbose_name="Отработанный день",
        blank=False,
        null=False)

    user = models.ForeignKey(
        User,
        verbose_name='Отчет пользователя',
        on_delete=models.CASCADE,
        blank=True,
        null=True)

    class Meta:
        verbose_name = 'Отчет'
        verbose_name_plural = 'Отчеты'


@receiver(post_save, sender=Report)
def update_user(sender, instance: Report, **kwargs):
    user = instance.user

    if user is not None:
        user = None
        return

    for entry in reversed(inspect.stack()):
        try:
            user = entry[0].f_locals['request'].user
            break
        except:
            pass

    if user is not None:
        instance.user = user
        instance.save()
