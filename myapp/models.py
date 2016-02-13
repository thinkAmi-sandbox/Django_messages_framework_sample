from django.db import models

class Item(models.Model):
    # 特に指定しない場合、blank=False(=入力必須)
    name = models.CharField('Name', max_length=255)