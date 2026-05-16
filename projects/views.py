from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy,reverse
from . import models
from . import forms
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

class ProjectListView(ListView):

    model = models.Project

    template_name = 'project/list.html'
    paginate_by = 3

    def get_queryset(self):

        query = self.request.GET.get('q',None)

        projects = models.Project.objects.all()

        if query:

            projects = projects.filter(
                title__icontains=query
            )

        return projects
    
class ProjectCreateView(LoginRequiredMixin, CreateView):

    model = models.Project

    form_class = forms.ProjectCreateForm

    template_name = 'project/create.html'

    success_url = reverse_lazy('project_list')

    def form_valid(self, form):

        form.instance.user = self.request.user

        return super().form_valid(form)

class ProjectUpdateView(LoginRequiredMixin,UpdateView):

    model = models.Project

    form_class = forms.ProjectUpdateForm

    template_name = 'project/update.html'

    context_object_name = 'project'

    def get_success_url(self):

        return reverse(
            'project_update',
            args=[self.object.id]
        )
    
class ProjectDeleteView(LoginRequiredMixin,DeleteView):

    model = models.Project

    template_name = 'project/delete.html'

    success_url = reverse_lazy('project_list')

class TaskCreateView(LoginRequiredMixin,CreateView):

    model = models.Task

    fields = ['description']

    template_name = 'project/task.html'

    def form_valid(self, form):

        project = get_object_or_404(
            models.Project,
            id=self.kwargs['pk']
)

        form.instance.project = project

        return super().form_valid(form)

    def get_success_url(self):

        return reverse(
            'project_update',
            args=[self.object.project.id]
        )



class TaskDeleteView(LoginRequiredMixin,DeleteView):

    model = models.Task

    template_name = 'project/delete.html'

    def get_success_url(self):

        return reverse(
            'project_update',
            args=[self.object.project.id]
        )
@login_required
def task_toggle(request, pk):

    task = get_object_or_404(
        models.Task,
        id=pk
    )

    task.is_completed = not task.is_completed

    task.save()

    return redirect(
        'project_update',
        pk=task.project.id
    )