from django import forms
from .models import MyModel

class formSerializer(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['input_file1', 'text_input1', 'text_input2', 'text_input3', 'text_input4']