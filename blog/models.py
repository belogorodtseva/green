from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()
    pic = models.ImageField(u"initial_picture",blank=True)

    def __str__(self):
        return self.title
