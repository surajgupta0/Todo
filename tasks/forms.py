# tasks/forms.py
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'priority', 'due_date']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter Title','class': 'form-control'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter Description','class': 'form-control','rows': 1}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local','class': 'form-control'}),
        }
    # def __init__(self, *args, **kwargs):
    #     super(TaskForm, self).__init__(*args, **kwargs)
    #     self.fields['title'].widget.attrs.update({
    #         'placeholder': 'Enter Title',
    #         'class': 'form-control',
    #     })
    #     self.fields['description'].widget.attrs.update({
    #         'placeholder': 'Enter Description',
    #         'class': 'form-control',
    #         'rows': 1,
    #     })
    #     self.fields['priority'].widget.attrs.update({
    #         'class': 'form-control',
    #     })
    #     self.fields['due_date'].widget.attrs.update({
    #         'class': 'form-control',
    #         'type': 'date',
    #     })
        