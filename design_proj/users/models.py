from django.db import models
from django.contrib.auth.models import AbstractUser


class AdvUser(AbstractUser):
    user_agreement = models.BooleanField('Пользовательское соглашение', default=False, db_index=True,
                                         help_text='Прочел и ознакомлен с <a href="http://www.sfmolga.ru/agreement.pdf'
                                                   '">Пользовательским соглашением</a>')

    class Meta(AbstractUser.Meta):
        pass

