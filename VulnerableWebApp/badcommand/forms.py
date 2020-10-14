from django import forms

class CommandForm(forms.Form):
    input_command = forms.CharField(label='Insert your ping command', max_length=200)
    
