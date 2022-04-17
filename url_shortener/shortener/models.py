from pyexpat import model
from django.db import models


class Urls(models.Model):
    short_id = models.SlugField(unique=True)
    http_url = models.URLField(
        max_length=255, 
        verbose_name='Сокращаемая ссылка')
    pub_date = models.DateTimeField(auto_now_add=True)
    nums_of_visits = models.IntegerField(default=0)
    want_edit = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.short_id}. Visits: {self.nums_of_visits}'

