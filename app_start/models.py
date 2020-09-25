from django.db import models
from ckeditor.fields import RichTextField


class PersonOfLivingSociety(models.Model):
    id_account = models.PositiveIntegerField()
    nick = models.TextField()
    avatar = models.URLField()
    steamid = models.BigIntegerField()
    url = models.URLField(default='None')
    role = models.CharField(max_length=16, default='user')


class News(models.Model):
    title = models.CharField(max_length=64, default='Отсутствует', null=False)
    title_tag = models.CharField(max_length=90, default='Отсутствует', null=False)
    author = models.TextField(editable=False, default='Администрация')
    text = RichTextField()
    news_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author) + ' | ' + str(self.news_date)

