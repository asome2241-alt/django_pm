from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=255)
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
    

    def __str__(self):
        return self.name


class ProjectStatus(models.IntegerChoices):
    PENDING = 1, _('Pending')
    COMPLETED = 2, _('Completed')
    POSTPONED = 3, _('Postponed')
    CANCELED = 4, _('Canceled')


class Project(models.Model):

    title = models.CharField(
        _('Title'),
        max_length=255
    )

    description = models.TextField(
        _('Description')
    )

    status = models.IntegerField(
        _('Status'),
        choices=ProjectStatus.choices,
        default=ProjectStatus.PENDING,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(
        Category,
        verbose_name=_('Category'),
        on_delete=models.PROTECT
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')

    def __str__(self):
        return self.title


class Task(models.Model):
    description = models.TextField(_('Description'))

    is_completed = models.BooleanField(default=False)

    project = models.ForeignKey(
        Project,
        verbose_name=_('Project'),
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _('Task')
        verbose_name_plural = _('Tasks')

    def __str__(self):
        return self.description