from django.db import models


class ToDoList(models.Model):
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.body[0:50]

    class Meta:
        ordering = ["-id"]
