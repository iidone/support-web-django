from django.db import models
import datetime
from django.utils.timezone import now 
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

        
        
class Problems(models.Model):
    problem = models.CharField('Название', max_length = 100)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='subproblems', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.problem}'
    
    class Meta:
        verbose_name = 'Проблема'
        verbose_name_plural = 'Проблемы'
        
        
class Issues(models.Model):
    pc_name = models.CharField('Имя компьютера', max_length = 255, default='Default PC name', null=True, blank=True)
    user_name = models.CharField('Имя пользователя', max_length = 255)
    issue = models.CharField('Название проблемы', max_length = 255)
    issue_description = models.CharField('Описание проблемы', max_length = 400)
    phone = models.CharField('Номер телефона', max_length = 150)    
    image = models.ImageField('Изображение проблемы', upload_to='main/images/', null=True, max_length=255)
    creation_time = models.DateTimeField("Дата и время создания заявки", default = now)
    closing_time = models.DateTimeField("Дата и время закрытия заявки", null=True, blank=True)
    status = models.CharField('Статус заявки', max_length = 100, default = "Не рассмотрена")
    
    
    
    
    def __str__(self):
        return f'Название: {self.issue}'

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url



class Moderators(models.Model):
    full_name = models.CharField('ФИО модератора', max_length = 100)
    mail = models.EmailField('Почта', max_length = 50, unique = True )
    month_tickets = models.IntegerField("Количество заявок в месяц", default = 0)

    def __str__(self):
        return f'Имя: {self.full_name}'

    class Meta:
        verbose_name = 'Модератор'
        verbose_name_plural = 'Модераторы'


class Directions(models.Model):
    issue  = models.CharField('Заявка', max_length = 100)
    moderator = models.CharField('Модератор', max_length = 100)

    def __str__(self):
        return f'Направление: {self.issue, self.moderator}'

    class Meta:
        verbose_name = 'Направление'
        verbose_name_plural = 'Направления'
        
        
        
@receiver(post_save, sender=User )
def create_moderator(sender, instance, created, **kwargs):
    if not created:
        full_name = f"{instance.first_name} {instance.last_name}"
        moderator, created = Moderators.objects.get_or_create(
            mail=instance.email.strip(),
            defaults={'full_name': full_name}
        )
        if created:
            print(f"Создан новый модератор: {full_name}")
        else:
            print(f"Модератор с почтой {instance.email} уже существует.")