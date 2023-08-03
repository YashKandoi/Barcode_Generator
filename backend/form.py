from django import forms

class DataInputForm(forms.Form):
    file_input = forms.FileField()
    Tax_Percentage = forms.CharField(max_length=100)
    Profit_Percentage = forms.CharField(max_length=100)
    # Open_Ai_input = forms.CharField(max_length=1000)  # Assuming the input is a text area

