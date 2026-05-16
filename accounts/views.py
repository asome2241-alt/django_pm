from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from django.shortcuts import redirect, render
from .forms import ProfileForm, UserRegisterForm
from django.contrib.auth.decorators import login_required


class RegisterView(CreateView):

    form_class = UserRegisterForm

    template_name = 'registration/register.html'

    success_url = reverse_lazy('project_list')

    def form_valid(self, form):

        response = super().form_valid(form)

        login(self.request, self.object)

        return response

@login_required
def edit_profile(request):

    form = ProfileForm(
        request.POST or None,
        instance=request.user
    )

    if request.method == 'POST':

        if form.is_valid():

            form.save()

            return redirect('profile')

    return render(
        request,
        'registration/profile.html',
        {'form': form}
    )