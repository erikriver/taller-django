from django import forms
from plus.models import Status

class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        exclude = ('author')
