from django import forms
from .models import SubModelForm


class SubModelFormAdd(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = SubModelForm
        fields = ['user_id', 'quiz_id', 'text']
