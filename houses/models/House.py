from django.db import models


class House(models.Model):

    name = models.CharField(max_length=255, verbose_name='Имя',)

    price = models.FloatField(verbose_name='Цена',)

    rating = models.IntegerField(verbose_name='Рейтинг', default=0,)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Дом'
        verbose_name_plural = 'Дома'
        ordering = ('-price', '-rating',)
