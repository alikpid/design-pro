from django.db import models

from .admin import AdvUser
from .utilities import get_timestamp_path
from django.core.validators import FileExtensionValidator
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, help_text="Укажите категорию")

    def __str__(self):
        return self.name


class Request(models.Model):
    day_add = models.DateField(null=True, blank=True)
    name = models.CharField(max_length=200, default='Отвали', verbose_name='Название', blank=False)
    summary = models.TextField(max_length=1000, help_text="Описание", blank=False)
    category = models.ForeignKey('category', help_text="Выбор категории", on_delete=models.CASCADE, blank=False)
    author = models.ForeignKey(AdvUser, on_delete=models.SET_NULL, null=True, blank=True)
    img = models.ImageField(max_length=200, upload_to=get_timestamp_path, blank=True, null=True,
                            validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])
    LOAN_STATUS = (
        ('n', 'Новая'),
        ('a', 'Принято в работу'),
        ('c', 'Выполнено'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='n')

    def get_status_name(self):
        for status in self.LOAN_STATUS:
            if status[0] == self.status:
                return status[1]
        return 'Не задан'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('order-detail', args=[str(self.id)])

    class Meta:
        ordering = ["status"]
        permissions = (("can_mark_returned", "Установите статус заказа"),)
