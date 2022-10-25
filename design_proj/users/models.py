from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser


class AdvUser(AbstractUser):
    surname = models.CharField(max_length=200, verbose_name='Фамилия', blank=False, validators=[
        RegexValidator(
            regex='^[А-Яа-я -]*$',
            message='Фамилия пользователя должна состоять из кириллицы, допускается дефис',
            code='invalid_username'
        ),
    ])
    name = models.CharField(max_length=200, verbose_name='Имя', blank=False, validators=[
        RegexValidator(
            regex='^[А-Яа-я -]*$',
            message='Имя пользователя должно состоять из кириллицы, допускается дефис',
            code='invalid_username'
        ),
    ])
    patronymic = models.CharField(max_length=200, verbose_name='Отчество', blank=True, validators=[
        RegexValidator(
            regex='^[А-Яа-я -]*$',
            message='Отчество пользователя должно состоять из кириллицы, допускается пробел',
            code='invalid_username'
        ),
    ])
    username = models.CharField(max_length=200, verbose_name='Логин', unique=True, blank=False, validators=[
        RegexValidator(
            regex='^[A-Za-z -]*$',
            message='Имя пользователя должно состоять только из латиницы, допускается дефис',
            code='invalid_username'
        ),
    ])
    email = models.EmailField(max_length=200, verbose_name='Почта', blank=False)
    user_agreement = models.BooleanField(default=False, db_index=True,
                                         help_text='Прочел и ознакомлен с <a href="http://www.sfmolga.ru/agreement.pdf'
                                                   '">Пользовательским соглашением</a>')

    class Meta(AbstractUser.Meta):
        pass

