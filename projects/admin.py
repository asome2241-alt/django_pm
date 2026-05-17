from django.contrib import admin
from django.db.models import Count

from . import models


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'status',
        'task_count',
        'created_at',
        'updated_at'
    )

    list_filter = (
        'status',
        'created_at',
        'updated_at'
    )

    search_fields = (
        'title',
        'description'
    )

    list_per_page = 20
    list_editable = (
        'status',
    )

    def get_queryset(self, request):

        qs = super().get_queryset(request)

        qs = qs.annotate(
            total_tasks=Count('task')
        )

        if request.user.is_superuser:
            return qs

        return qs.filter(user=request.user)

    def task_count(self, obj):

        return obj.total_tasks

    task_count.short_description = 'Tasks'


@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):

    list_display = ('id', 'description', 'is_completed', 'project')
       

    list_filter = (
        'is_completed',
    )

    search_fields = (
        'description',
    )
    list_editable = (
        'is_completed',
    )

    def get_queryset(self, request):

        qs = super().get_queryset(request)

        if request.user.is_superuser:
            return qs

        return qs.filter(project__user=request.user)


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'project_count'
    )

    search_fields = (
        'name',
    )

    def get_queryset(self, request):

        qs = super().get_queryset(request)

        qs = qs.annotate(
            total_projects=Count('project')
        )

        if request.user.is_superuser:
            return qs

        return qs.filter(
            project__user=request.user
        ).distinct()

    def project_count(self, obj):

        return obj.total_projects

    project_count.short_description = 'Projects'