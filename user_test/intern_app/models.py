from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


from intern_app.utils import define_exp_date
import uuid


class RefToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name = 'Пользователь')
    ref_token = models.UUIDField(default=uuid.uuid4, unique=True)
    creation_date = models.DateField(auto_now=True, verbose_name = 'Дата создания')
    exp_date = models.DateField(default=define_exp_date, verbose_name = 'Дата истечения срока')
    
    
    def __str__(self):
        return f'{self.user} {self.ref_token } '

    






