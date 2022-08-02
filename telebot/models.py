from django.db import models


class TeleSettings(models.Model):
    """Model for telegram connection"""
    tg_token = models.CharField(max_length=200, verbose_name='Токен')
    tg_chat = models.CharField(max_length=200, verbose_name='id чата')
    tg_text = models.TextField(verbose_name='Текст')

    def __str__(self):
        return self.tg_text

    class Meta:
        verbose_name = 'Настройку'
        verbose_name_plural = 'Настройки'
