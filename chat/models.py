from django.db import models

# Create your models here.


class MessageHistory(models.Model):
    message = models.CharField(max_length=1000, verbose_name='Сообщение')
    chat = models.ForeignKey('ChatRoom', on_delete=models.CASCADE, verbose_name='Чат')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

class ChatRoom(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название чата')

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'


