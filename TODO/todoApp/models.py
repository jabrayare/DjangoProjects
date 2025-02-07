from django.db import models


class task(models.Model):
    title = models.CharField(max_length=20)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
