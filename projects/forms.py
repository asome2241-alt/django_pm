from django import forms
from django.utils.translation import gettext_lazy as _

from . import models


attrs = {
    'class': 'form-control'
}


class ProjectCreateForm(forms.ModelForm):

    category = forms.ModelChoiceField(
        label=_('Category'),
        queryset=models.Category.objects.all(),
        widget=forms.Select(attrs=attrs)
    )

    title = forms.CharField(
        label=_('Title'),
        widget=forms.TextInput(attrs=attrs)
    )

    description = forms.CharField(
        label=_('Description'),
        widget=forms.Textarea(attrs=attrs)
    )

    class Meta:

        model = models.Project

        fields = [
            'category',
            'title',
            'description',
        ]


class ProjectUpdateForm(forms.ModelForm):

    category = forms.ModelChoiceField(
        label=_('Category'),
        queryset=models.Category.objects.all(),
        widget=forms.Select(attrs=attrs)
    )

    title = forms.CharField(
        label=_('Title'),
        widget=forms.TextInput(attrs=attrs)
    )

    description = forms.CharField(
        label=_('Description'),
        widget=forms.Textarea(attrs=attrs)
    )

    status = forms.ChoiceField(
        label=_('Status'),
        choices=models.ProjectStatus.choices,
        widget=forms.Select(attrs=attrs)
    )

    class Meta:

        model = models.Project

        fields = [
            'category',
            'title',
            'description',
            'status',
        ]