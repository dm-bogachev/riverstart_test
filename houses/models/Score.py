from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .House import House


class Score(models.Model):

    properties = ['p_location', 'p_quality', 'p_ecology', 'p_price', 'p_look']

    p_location = models.SmallIntegerField(verbose_name='Удобство расположения',
                                          validators=[
                                              MaxValueValidator(10),
                                              MinValueValidator(1)
                                          ],
                                          blank=True,
                                          null=True,)

    p_quality = models.SmallIntegerField(verbose_name='Состояние коммуникаций',
                                         validators=[
                                             MaxValueValidator(10),
                                             MinValueValidator(1)
                                         ],
                                         blank=True,
                                         null=True,)

    p_ecology = models.SmallIntegerField(verbose_name='Экологическая обстановка',
                                         validators=[
                                             MaxValueValidator(10),
                                             MinValueValidator(1)
                                         ],
                                         blank=True,
                                         null=True,)

    p_price = models.SmallIntegerField(verbose_name='Стоимость',
                                       validators=[
                                           MaxValueValidator(10),
                                           MinValueValidator(1)
                                       ],
                                       blank=True,
                                       null=True,)

    p_look = models.SmallIntegerField(verbose_name='Внешний вид',
                                      validators=[
                                          MaxValueValidator(10),
                                          MinValueValidator(1)
                                      ],
                                      blank=True,
                                      null=True,)

    house = models.ForeignKey(
        House, on_delete=models.CASCADE, verbose_name='Дом')

    date = models.DateTimeField(auto_now=True, verbose_name='Дата')

    def __str__(self):
        return str(self.house) + '/' + str(self.date)

    def save(self):
        rating = 0
        count = 0
        for property in self.properties:
            value = getattr(self, property)
            if value:
                rating += value
                count += 1
        self.house.rating += round(rating/count)
        self.house.save()
        return super().save()

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'
