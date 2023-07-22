from django import forms

class DataInputForm(forms.Form):
    file_input = forms.FileField()
    text_input1 = forms.CharField(max_length=100)
    text_input2 = forms.CharField(max_length=100)
    text_input3 = forms.CharField(max_length=100)
    text_input4 = forms.CharField(max_length=100)