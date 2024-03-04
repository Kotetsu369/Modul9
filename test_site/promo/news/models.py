from django.db import models


class Articles(models.Model):
    title = models.CharField ('Адрес', max_length=250)
    anons = models.CharField ('Кто посещал', max_length=100)
    full_text = models.TextField('Итоги акции')
    date = models.DateTimeField('Дата посещения')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Промо-акции'
        verbose_name_plural = 'Промо-акция'
