from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Project(models.Model):

    PENDING = 1
    COMPLETED = 2
    POSTPONED = 3
    CANCELED = 4

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (COMPLETED, 'Completed'),
        (POSTPONED, 'Postponed'),
        (CANCELED, 'Canceled'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()

    status = models.IntegerField(
        choices=STATUS_CHOICES,
        default=PENDING
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title


class Task(models.Model):
    description = models.TextField()

    is_completed = models.BooleanField(default=False)

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.description