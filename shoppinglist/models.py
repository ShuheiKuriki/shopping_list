# Create your models here.
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

class Shopping(models.Model):
    name = models.CharField('買う物', max_length=256, blank=True)
    shop = models.CharField('店', max_length=256, blank=True)
    date = models.DateField('最後に買った日', blank=True, null=True)
    days = models.IntegerField('最後に買ってからの経過日数', blank=True,null=True)
    buy_or_not = models.BooleanField('購入済', default=False)
    price = models.IntegerField('価格', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name