from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Текст')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата последнего редактирования')
    image = models.ImageField(upload_to='post_images/%Y/%m/%d', blank=True, verbose_name='Картинка')

    class Meta:
        ordering = '-created',

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogapp:detail', kwargs={'pk': self.pk})

# help_text
