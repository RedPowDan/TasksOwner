from django.db import models

from tasks.base_models import BaseModel
from tasks.models import Report


class ReportInTask(BaseModel):
    HOURS_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8)
    )
    amount_hours = models.IntegerField(
        verbose_name="Кол-во затраченных часов",
        choices=HOURS_CHOICES,
        blank=False,
        null=False)

    comment = models.CharField(
        verbose_name="Комментарий",
        max_length=300,
        blank=True,
        null=False)

    report = models.ForeignKey(Report, verbose_name="Отчет", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Отчет'
        verbose_name_plural = 'Отчеты'
