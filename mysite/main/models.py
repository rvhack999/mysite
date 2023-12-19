from django.db import models


class User(models.Model):
    name = models.CharField(max_length=20, help_text='Name')
    email = models.EmailField(help_text='email', null=True, blank=True)
    phone = models.CharField(max_length=20, help_text='phone')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
    def __str__(self):
        return self.name
# Create your models here.
