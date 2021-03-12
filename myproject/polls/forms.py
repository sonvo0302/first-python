# forms.py
from django import forms

from .models import Question, Choice


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ChoiceForm, self).__init__(*args, **kwargs)
        self.fields['question'].empty_label = "Select"

