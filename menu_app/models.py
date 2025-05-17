from django.db import models
from django.urls import reverse, NoReverseMatch

class MenuItem(models.Model):
    name = models.CharField(max_length=100)  # Название меню
    title = models.CharField(max_length=100)  # Заголовок пункта
    url = models.CharField(max_length=200)  # URL или named URL
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    order = models.IntegerField(default=0)  # Порядок отображения

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.name} - {self.title}"

    def get_url(self):
        if self.url.startswith('/'):
            return self.url
        try:
            return reverse(self.url)
        except NoReverseMatch:
            return '#'
